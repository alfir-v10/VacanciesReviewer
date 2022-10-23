import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import config
from utils import getVacanciesLikeObject, get_engine, getVacanciesLikeJson, getTimeInterval
import HeadHunterVacancyDescription as vc
import HeadHunterDatabaseDescription as db
from sqlalchemy_utils.functions import get_primary_keys
from sqlalchemy.orm.util import identity_key
import time


def add_row(row, session):
    try:
        session.add(row)
        session.commit()
    except Exception as e:
        print(e)
        session.rollback()


def session_commit(session):
    try:
        session.commit()
    except Exception as e:
        print(e)
        session.rollback()


def get_by_key(session, table, column, key):
    return session.query(table).filter(column == key).all()


def runCrawler(text_list, date_from, date_to, weeks=0, days=0, hours=0, minutes=0, seconds=0, per_page=100):
    for text in text_list:
        total_found = 0
        dublicates_founded = 0
        new_vacancies = 0
        intervals = getTimeInterval(date_from=date_from, date_to=date_to, weeks=weeks, days=days,
                                    hours=hours, minutes=minutes, seconds=seconds)
        if intervals:
            for datefrom, dateto in intervals:
                data = getVacanciesLikeJson(text, per_page=per_page, date_from=datefrom, date_to=dateto)
                pages = data['pages']
                per_page = data['per_page']
                found = data['found']
                print(f'From {datefrom} to {dateto} are founded {found} vacancies.')
                total_found += found
                for p in range(0, pages + 1):
                    print(f'Page: {p}/{pages}')
                    data = getVacanciesLikeJson(text, per_page=100, page=p, date_from=datefrom, date_to=dateto)
                    items = data['items']
                    engine = get_engine(user=config.DATABASE.get('user'),
                                        password=config.DATABASE.get('password'),
                                        host=config.DATABASE.get('host'),
                                        port=config.DATABASE.get('port'),
                                        database_name=config.DATABASE.get('database_name'),
                                        driver_name=config.DATABASE.get('driver_name'),
                                        driver=config.DATABASE.get('driver'))
                    Session = sessionmaker(bind=engine)
                    session = Session()

                    saved_items = []
                    for item in items:
                        if not get_by_key(session, db.Vacancy, db.Vacancy.vacancy_id, item['id']):
                            saved_items.append(item)
                    len_save_items = len(saved_items)
                    new_vacancies += len(saved_items)
                    dublicates_founded += len(items) - len_save_items
                    print(f'Founded {len(items) - len_save_items} dublicates, and {len_save_items} new vacancies')
                    print(f'Total new vacancies: {new_vacancies}\t Total dublicates: {dublicates_founded}\t Total found: {total_found}')
                    vacancy_count = 0
                    for item in saved_items:
                        vacancy = vc.VacancyInfoByVacancyPage(vacancy=item)
                        vacancy_count += 1
                        print(f'New vacancy add: {vacancy_count}/{len_save_items}')
                        time.sleep(1)
                        if not get_by_key(session, db.TypeVacancy, db.TypeVacancy.type_id, vacancy.type_id):
                            type_vacancy_add = db.TypeVacancy(type_id=vacancy.type_id,
                                                              type_name=vacancy.type_name)
                            add_row(type_vacancy_add, session)
                        type_vacancy_id = get_by_key(session, db.TypeVacancy, db.TypeVacancy.type_id, vacancy.type_id)[
                            0].id

                        if not get_by_key(session, db.Department, db.Department.department_id, vacancy.department_id):
                            department_add = db.Department(department_id=vacancy.department_id,
                                                           department_name=vacancy.department_name)
                            add_row(department_add, session)
                        department_id = \
                            get_by_key(session, db.Department, db.Department.department_id, vacancy.department_id)[
                                0].id

                        if not get_by_key(session, db.Area, column=db.Area.area_id, key=vacancy.area_id):
                            area_add = db.Area(area_id=vacancy.area_id,
                                               area_name=vacancy.area_name,
                                               area_url=vacancy.area_url)
                            add_row(area_add, session)
                        area_id = get_by_key(session, db.Area, column=db.Area.area_id, key=vacancy.area_id)[0].id

                        if not get_by_key(session, db.Metro, db.Metro.station_id, vacancy.station_id):
                            metro_add = db.Metro(station_id=vacancy.station_id,
                                                 station_name=vacancy.station_name,
                                                 line_id=vacancy.line_id,
                                                 line_name=vacancy.line_name,
                                                 station_latitude=vacancy.station_latitude,
                                                 station_longitude=vacancy.station_longitude)
                            add_row(metro_add, session)
                        metro_id = get_by_key(session, db.Metro, db.Metro.station_id, vacancy.station_id)[0].id

                        if not get_by_key(session, db.Employer, db.Employer.employer_id, vacancy.employer_id):
                            employer_add = db.Employer(employer_id=vacancy.employer_id,
                                                       employer_name=vacancy.employer_name,
                                                       employer_trusted=vacancy.employer_trusted,
                                                       employer_url=vacancy.employer_url,
                                                       employer_vacancies_url=vacancy.employer_vacancies_url)
                            add_row(employer_add, session)
                        employer_id = get_by_key(session, db.Employer, db.Employer.employer_id, vacancy.employer_id)[
                            0].id

                        if not get_by_key(session, db.Employment, db.Employment.employment_id, vacancy.employment_id):
                            employment_add = db.Employment(employment_id=vacancy.employment_id,
                                                           employment_name=vacancy.employment_name)
                            add_row(employment_add, session)
                        employment_id = \
                            get_by_key(session, db.Employment, db.Employment.employment_id, vacancy.employment_id)[
                                0].id

                        if not get_by_key(session, db.Schedule, db.Schedule.schedule_id, vacancy.schedule_id):
                            schedule_add = db.Schedule(schedule_id=vacancy.schedule_id,
                                                       schedule_name=vacancy.schedule_name)
                            add_row(schedule_add, session)
                        schedule_id = get_by_key(session, db.Schedule, db.Schedule.schedule_id, vacancy.schedule_id)[
                            0].id

                        if not get_by_key(session, db.BillingType, db.BillingType.billing_type_id,
                                          vacancy.billing_type_id):
                            billing_type_add = db.BillingType(billing_type_id=vacancy.billing_type_id,
                                                              billing_type_name=vacancy.billing_type_name)
                            add_row(billing_type_add, session)
                        billing_type_id = \
                            get_by_key(session, db.BillingType, db.BillingType.billing_type_id,
                                       vacancy.billing_type_id)[
                                0].id

                        if not get_by_key(session, db.Experience, db.Experience.experience_id, vacancy.experience_id):
                            experience_add = db.Experience(experience_id=vacancy.experience_id,
                                                           experience_name=vacancy.experience_name)
                            add_row(experience_add, session)
                        experience_id = \
                            get_by_key(session, db.Experience, db.Experience.experience_id, vacancy.experience_id)[
                                0].id

                        if not get_by_key(session, db.InsiderInterview, db.InsiderInterview.insider_interview_id,
                                          vacancy.insider_interview_id):
                            insider_interview_add = db.InsiderInterview(
                                insider_interview_id=vacancy.insider_interview_id,
                                insider_interview_url=vacancy.insider_interview_url)
                            add_row(insider_interview_add, session)
                        insider_interview_id = \
                            get_by_key(session, db.InsiderInterview, db.InsiderInterview.insider_interview_id,
                                       vacancy.insider_interview_id)[0].id

                        vacancy_add = db.Vacancy(vacancy_id=vacancy.vacancy_id,
                                                 name=vacancy.name,
                                                 department_id=department_id,
                                                 type_id=type_vacancy_id,
                                                 area_id=area_id,
                                                 has_test=vacancy.has_test,
                                                 premium=vacancy.premium,
                                                 archived=vacancy.archived,
                                                 allow_messages=vacancy.allow_messages,
                                                 response_letter_required=vacancy.response_letter_required,
                                                 accept_handicapped=vacancy.accept_handicapped,
                                                 accept_kids=vacancy.accept_kids,
                                                 created_at=vacancy.created_at,
                                                 published_at=vacancy.published_at,
                                                 hidden=vacancy.hidden,
                                                 accept_incomplete_resumes=vacancy.accept_incomplete_resumes,
                                                 accept_temporary=vacancy.accept_temporary,
                                                 quick_responses_allowed=vacancy.quick_responses_allowed,
                                                 sort_point_distanse=vacancy.sort_point_distanse,
                                                 station_id=metro_id,
                                                 employer_id=employer_id,
                                                 employment_id=employment_id,
                                                 schedule_id=schedule_id,
                                                 billing_type_id=billing_type_id,
                                                 experience_id=experience_id,
                                                 insider_interview_id=insider_interview_id,
                                                 snippet_requirements=vacancy.snippet_requirements,
                                                 snippet_responsibility=vacancy.snippet_responsibility,
                                                 vacancy_description=vacancy.vacancy_description,
                                                 vacancy_code=vacancy.vacancy_code,
                                                 url=vacancy.url,
                                                 response_url=vacancy.response_url,
                                                 )
                        add_row(vacancy_add, session)

                        if vacancy.driver_license_types:
                            for dictionary in vacancy.driver_license_types:
                                drive = vc.DriverLicense(dictionary)
                                driver_add = db.DriverLicenseTypes(vacancy_id=vacancy_add.id,
                                                                   license_id=drive.license_id)
                                session.add(driver_add)
                            session_commit(session)

                        if vacancy.languages:
                            for dictionary in vacancy.languages:
                                lang = vc.Language(dictionary)
                                if not get_by_key(session, db.LanguagesLevel, db.LanguagesLevel.language_level_id,
                                                  lang.language_level_id):
                                    lang_level_add = db.LanguagesLevel(language_level_id=lang.language_level_id,
                                                                       language_level_name=lang.language_level_name)

                                    session.add(lang_level_add)
                                    session_commit(session)

                                if not get_by_key(session, db.LanguagesName, db.LanguagesName.language_id,
                                                  lang.language_id):
                                    lang_name_add = db.LanguagesName(language_id=lang.language_id,
                                                                     language_name=lang.language_name)

                                    session.add(lang_name_add)
                                    session_commit(session)

                                lang_add = db.Languages(vacancy_id=vacancy_add.id,
                                                        language_id=get_by_key(session, db.LanguagesName,
                                                                               db.LanguagesName.language_id,
                                                                               lang.language_id)[0].id,
                                                        language_level_id=get_by_key(session, db.LanguagesLevel,
                                                                                     db.LanguagesLevel.language_level_id,
                                                                                     lang.language_level_id)[0].id)
                                session.add(lang_add)
                                session_commit(session)

                        if vacancy.specializations:
                            for dictionary in vacancy.specializations:
                                spec = vc.Specialization(dictionary)
                                if not get_by_key(session, db.ProfArea, db.ProfArea.profarea_id, spec.profarea_id):
                                    prof_area_add = db.ProfArea(profarea_id=spec.profarea_id,
                                                                profarea_name=spec.profarea_name)
                                    session.add(prof_area_add)
                                    session_commit(session)

                                if not get_by_key(session, db.SpecializationsName, db.SpecializationsName.name,
                                                  spec.name):
                                    spec_name_add = db.SpecializationsName(name=spec.name)
                                    session.add(spec_name_add)
                                    session.commit()

                                spec_add = db.Specializations(vacancy_id=vacancy_add.id,
                                                              name=get_by_key(session, db.SpecializationsName,
                                                                              db.SpecializationsName.name, spec.name)[
                                                                  0].id,
                                                              profarea_id=get_by_key(session, db.ProfArea,
                                                                                     db.ProfArea.profarea_id,
                                                                                     spec.profarea_id)[0].id)
                                session.add(spec_add)
                                session_commit(session)

                        if vacancy.professional_roles:
                            for dictionary in vacancy.professional_roles:
                                prof_role = vc.ProfessionalRole(dictionary)
                                if not get_by_key(session, db.Roles, db.Roles.role_name,
                                                  prof_role.role_name):
                                    role_add = db.Roles(role_id=prof_role.role_id,
                                                        role_name=prof_role.role_name)
                                    session.add(role_add)
                                    session_commit(session)

                                prof_role_add = db.ProfessionalRoles(vacancy_id=vacancy_add.id,
                                                                     role_id=get_by_key(session, db.Roles,
                                                                                        db.Roles.role_name,
                                                                                        prof_role.role_name)[0].id)
                                session.add(prof_role_add)
                                session_commit(session)

                        if vacancy.key_skills:
                            for dictionary in vacancy.key_skills:

                                key_skill = vc.KeySkills(dictionary)

                                if not get_by_key(session, db.Skills, db.Skills.skill, key_skill.key_skill_name):
                                    skill_add = db.Skills(skill=key_skill.key_skill_name)
                                    session.add(skill_add)
                                    session_commit(session)

                                key_skill_add = db.KeySkills(vacancy_id=vacancy_add.id,
                                                             skill=get_by_key(session, db.Skills, db.Skills.skill,
                                                                              key_skill.key_skill_name)[0].id)
                                session.add(key_skill_add)
                            session_commit(session)

                        if vacancy.salary:
                            salary_add = db.Salary(vacancy_id=vacancy_add.id,
                                                   salary_to=vacancy.salary_to,
                                                   salary_from=vacancy.salary_from,
                                                   salary_currency=vacancy.salary_currency,
                                                   salary_gross=vacancy.salary_gross)
                            add_row(salary_add, session)

                        if vacancy.contacts:
                            contacts_add = db.Contacts(vacancy_id=vacancy_add.id,
                                                       contact_name=vacancy.contact_name,
                                                       contacts_email=vacancy.contacts_email)
                            add_row(contacts_add, session)

                        if vacancy.contacts_phones:
                            for dictionary in vacancy.contacts_phones:
                                phone = vc.Phones(dictionary)
                                phone_add = db.Phones(vacancy_id=vacancy_add.id,
                                                      country=phone.country,
                                                      city=phone.city,
                                                      number=phone.number,
                                                      comment=phone.comment)
                                session.add(phone_add)
                            session_commit(session)

                        if vacancy.address:
                            address_add = db.Address(vacancy_id=vacancy_add.id,
                                                     city=vacancy.city,
                                                     street=vacancy.street,
                                                     building=vacancy.building,
                                                     address_description=vacancy.address_description,
                                                     address_latitude=vacancy.address_latitude,
                                                     address_longitude=vacancy.address_longitude,
                                                     address_raw=vacancy.address_raw)
                            add_row(address_add, session)

                        if vacancy.metro_stations:
                            for dictionary in vacancy.metro_stations:
                                station = vc.Metro(dictionary)
                                station_add = db.MetroStations(vacancy_id=vacancy_add.id,
                                                               station_id=station.station_id,
                                                               station_name=station.station_name,
                                                               line_id=station.line_id,
                                                               line_name=station.line_name,
                                                               station_latitude=station.station_latitude,
                                                               station_longitude=station.station_longitude)
                                session.add(station_add)
                            session_commit(session)

                        if vacancy.working_days:
                            for dictionary in vacancy.working_days:
                                working_day = vc.Working(dictionary)
                                working_day_add = db.WorkingDays(vacancy_id=vacancy_add.id,
                                                                 day_id=working_day.work_id,
                                                                 day_name=working_day.work_name)
                                session.add(working_day_add)
                            session_commit(session)

                        if vacancy.working_time_intervals:
                            for dictionary in vacancy.working_time_intervals:
                                working_time = vc.Working(dictionary)
                                working_time_add = db.WorkingTimeIntervals(vacancy_id=vacancy_add.id,
                                                                           interval_id=working_time.work_id,
                                                                           interval_name=working_time.work_name)
                                session.add(working_time_add)
                            session_commit(session)

                        if vacancy.working_time_modes:
                            for dictionary in vacancy.working_time_modes:
                                working_modes = vc.Working(dictionary)
                                working_modes_add = db.WorkingTimeModes(vacancy_id=vacancy_add.id,
                                                                        mode_id=working_modes.work_id,
                                                                        mode_name=working_modes.work_name)
                                session.add(working_modes_add)
                            session_commit(session)
                    session.close()
                    time.sleep(5)
            time.sleep(30)
        print(
            f'For request \"{text}\" are founded:'
            f'\n\tnew vacancies: {new_vacancies}'
            f'\n\tdublicates: {dublicates_founded}'
            f'\n\ttotal found: {total_found}')


if __name__ == '__main__':
    text_list = ['python']
    date_from = '2022-09-28T12:00:00'
    date_to = '2022-10-23T00:00:00'
    runCrawler(text_list, date_from=date_from, date_to=date_to, weeks=0, days=1, hours=6, minutes=0, seconds=0)
