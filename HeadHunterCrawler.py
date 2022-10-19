import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import config
from utils import getVacancies, get_engine
import HeadHunterVacancyDescription as vc
import HeadHunterDatabaseDescription as db
from sqlalchemy_utils.functions import get_primary_keys
from sqlalchemy.orm.util import identity_key


def check_primary_key(table, key, session):
    keys = get_primary_keys(table)
    keys = identity_key(table, key)
    m = session.identity_map.items()
    l = session.identity_map.get(keys)
    if key in keys:
        return True
    return False


def add_row(row, session):
    try:
        session.add(row)
        session.commit()
    except Exception as e:
        session.rollback()
        print(e)

def session_commit(session):
    try:
        session.commit()
    except Exception as e:
        session.rollback()
        print(e)

if __name__ == '__main__':
    text = 'data science'
    data = getVacancies(text, per_page=5)
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
    for item in items:

        vacancy = vc.VacancyInfoByVacancyPage(vacancy=item)

        type_vacancy_add = db.TypeVacancy(type_id=vacancy.type_id,
                                          type_name=vacancy.type_name)
        add_row(type_vacancy_add, session)

        department_add = db.Department(department_id=vacancy.department_id,
                                       department_name=vacancy.department_name)
        add_row(department_add, session)

        area_add = db.Area(area_id=vacancy.area_id,
                           area_name=vacancy.area_name,
                           area_url=vacancy.area_url)
        add_row(area_add, session)

        metro_add = db.Metro(station_id=vacancy.station_id,
                             station_name=vacancy.station_name,
                             line_id=vacancy.line_id,
                             line_name=vacancy.line_name,
                             station_latitude=vacancy.station_latitude,
                             station_longitude=vacancy.station_longitude)
        add_row(metro_add, session)

        employer_add = db.Employer(employer_id=vacancy.employer_id,
                                   employer_name=vacancy.employer_name,
                                   employer_trusted=vacancy.employer_trusted,
                                   employer_url=vacancy.employer_url,
                                   employer_vacancies_url=vacancy.employer_vacancies_url)
        add_row(employer_add, session)

        employment_add = db.Employment(employment_id=vacancy.employment_id,
                                       employment_name=vacancy.employment_name)
        add_row(employment_add, session)

        schedule_add = db.Schedule(schedule_id=vacancy.schedule_id,
                                   schedule_name=vacancy.schedule_name)
        add_row(schedule_add, session)

        billing_type_add = db.BillingType(billing_type_id=vacancy.billing_type_id,
                                          billing_type_name=vacancy.billing_type_name)
        add_row(billing_type_add, session)

        experience_add = db.Experience(experience_id=vacancy.experience_id,
                                       experience_name=vacancy.experience_name)
        add_row(experience_add, session)

        insider_interview_add = db.InsiderInterview(insider_interview_id=vacancy.insider_interview_id,
                                                    insider_interview_url=vacancy.insider_interview_url)
        add_row(insider_interview_add, session)

        vacancy_add = db.Vacancy(vacancy_id=vacancy.vacancy_id,
                                 name=vacancy.name,
                                 department_id=department_add.id,
                                 type_id=type_vacancy_add.id,
                                 area_id=area_add.id,
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
                                 station_id=metro_add.id,
                                 employer_id=employer_add.id,
                                 employment_id=employment_add.id,
                                 schedule_id=schedule_add.id,
                                 billing_type_id=billing_type_add.id,
                                 experience_id=experience_add.id,
                                 insider_interview_id=insider_interview_add.id,
                                 snippet_requirements=vacancy.snippet_requirements,
                                 snippet_responsibility=vacancy.snippet_responsibility,
                                 vacancy_description=vacancy.vacancy_description,
                                 vacancy_code=vacancy.vacancy_code,
                                 url=vacancy.url,
                                 response_url=vacancy.response_url,
                                 )
        add_row(vacancy_add, session)

        if vacancy.driver_license_types:
            for obj in vacancy.driver_license_types:
                drive = vc.DriverLicense(obj)
                driver_add = db.DriverLicenseTypes(vacancy_id=vacancy_add.id,
                                                   license_id=drive.license_id)
                session.add(driver_add)
            session_commit(session)

        if vacancy.languages:
            for obj in vacancy.languages:
                lang = vc.Language(obj)
                lang_level_add = db.LanguagesLevel(language_level_id=lang.language_level_id,
                                                   language_level_name=lang.language_level_name)

                lang_name_add = db.LanguagesName(language_id=lang.language_id,
                                                 language_name=lang.language_name)

                lang_add = db.Languages(vacancy_id=vacancy_add.id,
                                        language_id=lang_name_add.id,
                                        language_level_id=lang_level_add.id)
                session.add(lang_level_add)
                session.add(lang_name_add)
                session.add(lang_add)
            session_commit(session)

        if vacancy.specializations:
            for obj in vacancy.specializations:
                spec = vc.Specialization(obj)
                prof_area_add = db.ProfArea(profarea_id=spec.profarea_id,
                                            profarea_name=spec.profarea_name)
                spec_add = db.Specializations(vacancy_id=vacancy_add.id,
                                              name=spec.name,
                                              profarea_id=prof_area_add.id)
                session.add(prof_area_add)
                session.add(spec_add)
            session_commit(session)

        if vacancy.professional_roles:
            for obj in vacancy.professional_roles:
                prof_role = vc.ProfessionalRole(obj)
                role_add = db.Roles(role_id=prof_role.role_id,
                                    role_name=prof_role.role_name)
                prof_role_add = db.ProfessionalRoles(vacancy_id=vacancy_add.id,
                                                     role_id=role_add.id)
                session.add(role_add)
                session.add(prof_role_add)
            session_commit(session)

        if vacancy.key_skills:
            for obj in vacancy.key_skills:
                key_skill = vc.KeySkills(obj)
                key_skill_add = db.KeySkills(vacancy_id=vacancy_add.id,
                                             skill=key_skill.key_skill_name)
                session.add(key_skill_add)
            session_commit(session)

        salary_add = db.Salary(vacancy_id=vacancy_add.id,
                               salary_to=vacancy.salary_to,
                               salary_from=vacancy.salary_from,
                               salary_currency=vacancy.salary_currency,
                               salary_gross=vacancy.salary_gross)
        add_row(salary_add, session)

        contacts_add = db.Contacts(vacancy_id=vacancy_add.id,
                                   contact_name=vacancy.contact_name,
                                   contacts_email=vacancy.contacts_email)
        add_row(contacts_add, session)

        if vacancy.contacts_phones:
            for obj in vacancy.contacts_phones:
                phone = vc.Phones(obj)
                phone_add = db.Phones(vacancy_id=vacancy_add.id,
                                      country=phone.country,
                                      city=phone.city,
                                      number=phone.number,
                                      comment=phone.comment)
                session.add(phone_add)
            session_commit(session)

        address_add = db.Address(vacancy_id=vacancy_add.id,
                                 address=vacancy.address,
                                 city=vacancy.city,
                                 street=vacancy.street,
                                 building=vacancy.building,
                                 address_description=vacancy.address_description,
                                 address_latitude=vacancy.address_latitude,
                                 address_longitude=vacancy.address_longitude,
                                 address_raw=vacancy.address_raw)
        add_row(address_add, session)

        if vacancy.metro_stations:
            for obj in vacancy.metro_stations:
                station = vc.Metro(obj)
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
            for obj in vacancy.working_days:
                working_day = vc.Working(obj)
                working_day_add = db.WorkingDays(vacancy_id=vacancy_add.id,
                                                 day_id=working_day.work_id,
                                                 day_name=working_day.work_name)
                session.add(working_day_add)
            session_commit(session)

        if vacancy.working_time_intervals:
            for obj in vacancy.working_time_intervals:
                working_time = vc.Working(obj)
                working_time_add = db.WorkingTimeIntervals(vacancy_id=vacancy_add.id,
                                                           interval_id=working_time.work_id,
                                                           interval_name=working_time.work_name)
                session.add(working_time_add)
            session_commit(session)

        if vacancy.working_time_modes:
            for obj in vacancy.working_time_modes:
                working_modes = vc.Working(obj)
                working_modes_add = db.WorkingTimeModes(vacancy_id=vacancy_add.id,
                                                        mode_id=working_modes.work_id,
                                                        mode_name=working_modes.work_name)
                session.add(working_modes_add)
            session_commit(session)
    session.close()

