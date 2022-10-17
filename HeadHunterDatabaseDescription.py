import config
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Vacancy(Base):
    __tablename__ = 'vacancies'
    vacancy_id = Column(String, primary_key=True)
    name = Column(String)
    department_id = Column(String, ForeignKey('department.department_id'))
    type_id = Column(String, ForeignKey('type_vacancy.type_id'))
    area_id = Column(String, ForeignKey('area.area_id'))
    has_test = Column(Boolean)
    premium = Column(Boolean)
    archived = Column(Boolean)
    allow_messages = Column(Boolean)
    response_letter_required = Column(Boolean)
    accept_handicapped = Column(Boolean)
    accept_kids = Column(Boolean)
    created_at = Column(String)
    published_at = Column(String)
    hidden = Column(Boolean)
    accept_incomplete_resumes = Column(Boolean)
    accept_temporary = Column(Boolean)
    quick_responses_allowed = Column(Boolean)
    sort_point_distanse = Column(String)
    station_id = Column(String, ForeignKey('metro.station_id'))
    employer_id = Column(String, ForeignKey('employer.employer_id'))
    employment_id = Column(String, ForeignKey('employment.employment_id'))
    schedule_id = Column(String, ForeignKey('schedule.schedule_id'))
    billing_type_id = Column(String, ForeignKey('billing_type.billing_type_id'))
    experience_id = Column(String, ForeignKey('experience.experience_id'))
    insider_interview_id = Column(String, ForeignKey('insider_interview.insider_interview_id'))
    snippet_requirements = Column(String)
    snippet_responsibility = Column(String)
    vacancy_description = Column(String)
    vacancy_code = Column(String)
    url = Column(String)
    response_url = Column(String)


class Languages(Base):
    __tablename__ = 'languages'
    idx = Column(Integer, primary_key=True)
    vacancy_id = Column(String, ForeignKey('vacancies.vacancy_id'))
    language_id = Column(String, ForeignKey('languages_name.language_id'))
    language_level_id = Column(String, ForeignKey('languages_level.language_level_id'))


class LanguagesName(Base):
    __tablename__ = 'languages_name'
    language_id = Column(String, primary_key=True)
    language_name = Column(String)


class LanguagesLevel(Base):
    __tablename__ = 'languages_level'
    language_level_id = Column(String, primary_key=True)
    language_level_name = Column(String)


class DriverLicenseTypes(Base):
    __tablename__ = 'driver_license_types'
    idx = Column(Integer, primary_key=True)
    vacancy_id = Column(String, ForeignKey('vacancies.vacancy_id'))
    license_id = Column(String)


class Specializations(Base):
    __tablename__ = 'specializations'
    idx = Column(Integer, primary_key=True)
    vacancy_id = Column(String, ForeignKey('vacancies.vacancy_id'))
    name = Column(String)
    profarea_id = Column(String, ForeignKey('profarea.profarea_id'))


class ProfArea(Base):
    __tablename__ = 'profarea'
    profarea_id = Column(String, primary_key=True)
    profarea_name = Column(String)


class ProfessionalRoles(Base):
    __tablename__ = 'professional_roles'
    idx = Column(Integer, primary_key=True)
    vacancy_id = Column(String, ForeignKey('vacancies.vacancy_id'))
    role_id = Column(String, ForeignKey('roles.role_id'))


class Roles(Base):
    __tablename__ = 'roles'
    role_id = Column(String, primary_key=True)
    role_name = Column(String)


class KeySkills(Base):
    __tablename__ = 'key_skills'
    idx = Column(Integer, primary_key=True)
    vacancy_id = Column(String, ForeignKey('vacancies.vacancy_id'))
    skill = Column(String)


class Employment(Base):
    __tablename__ = 'employment'
    employment_id = Column(String, primary_key=True)
    employment_name = Column(String)


class Experience(Base):
    __tablename__ = 'experience'
    experience_id = Column(String, primary_key=True)
    experience_name = Column(String)


class InsiderInterview(Base):
    __tablename__ = 'insider_interview'
    insider_interview_id = Column(String, primary_key=True)
    insider_interview_url = Column(String)


class BillingType(Base):
    __tablename__ = 'billing_type'
    billing_type_id = Column(String, primary_key=True)
    billing_type_name = Column(String)


class Schedule(Base):
    __tablename__ = 'schedule'
    schedule_id = Column(String, primary_key=True)
    schedule_name = Column(String)


class Salary(Base):
    __tablename__ = 'salary'
    idx = Column(Integer, primary_key=True)
    vacancy_id = Column(String, ForeignKey('vacancies.vacancy_id'))
    salary_to = Column(String)
    salary_from = Column(String)
    salary_currency = Column(String)
    salary_gross = Column(Boolean)


class Employer(Base):
    __tablename__ = 'employer'
    employer_id = Column(String, primary_key=True)
    employer_name = Column(String)
    employer_trusted = Column(String)
    employer_url = Column(String)
    employer_vacancies_url = Column(String)


class Contacts(Base):
    __tablename__ = 'contacts'
    idx = Column(Integer, primary_key=True)
    vacancy_id = Column(String, ForeignKey('vacancies.vacancy_id'))
    contact_name = Column(String)
    contacts_email = Column(String)


class Phones(Base):
    __tablename__ = 'phones'
    idx = Column(Integer, primary_key=True)
    vacancy_id = Column(String, ForeignKey('vacancies.vacancy_id'))
    country = Column(String)
    city = Column(String)
    number = Column(String)
    comment = Column(String)


class Area(Base):
    __tablename__ = 'area'
    area_id = Column(String, primary_key=True)
    area_name = Column(String)
    area_url = Column(String)


class TypeVacancy(Base):
    __tablename__ = 'type_vacancy'
    type_id = Column(String, primary_key=True)
    type_name = Column(String)


class Address(Base):
    __tablename__ = 'address'
    idx = Column(Integer, primary_key=True)
    vacancy_id = Column(String, ForeignKey('vacancies.vacancy_id'))
    address = Column(String)
    city = Column(String)
    street = Column(String)
    building = Column(String)
    address_description = Column(String)
    address_latitude = Column(String)
    address_longitude = Column(String)
    address_raw = Column(String)


class Metro(Base):
    __tablename__ = 'metro'
    station_id = Column(String, primary_key=True)
    station_name = Column(String)
    line_id = Column(String)
    line_name = Column(String)
    station_latitude = Column(String)
    station_longitude = Column(String)


class MetroStations(Base):
    __tablename__ = 'metro_stations'
    idx = Column(Integer, primary_key=True)
    vacancy_id = Column(String, ForeignKey('vacancies.vacancy_id'))
    station_id = Column(String, ForeignKey('metro.station_id'))
    station_name = Column(String)
    line_id = Column(String)
    line_name = Column(String)
    station_latitude = Column(String)
    station_longitude = Column(String)


class Department(Base):
    __tablename__ = 'department'
    department_id = Column(String, primary_key=True)
    department = Column(String)
    department_name = Column(String)


class WorkingDays(Base):
    __tablename__ = 'working_days'
    idx = Column(Integer, primary_key=True)
    vacancy_id = Column(String, ForeignKey('vacancies.vacancy_id'))
    day_id = Column(String)
    day_name = Column(String)


class WorkingTimeIntervals(Base):
    __tablename__ = 'working_time_intervals'
    idx = Column(Integer, primary_key=True)
    vacancy_id = Column(String, ForeignKey('vacancies.vacancy_id'))
    interval_id = Column(String)
    interval_name = Column(String)


class WorkingTimeModes(Base):
    __tablename__ = 'working_time_modes'
    idx = Column(Integer, primary_key=True)
    vacancy_id = Column(String, ForeignKey('vacancies.vacancy_id'))
    mode_id = Column(String)
    mode_name = Column(String)


if __name__ == "__main__":
    from sqlalchemy.orm import sessionmaker
    from get_engine import get_engine

    engine = get_engine(user=config.DATABASE.get('user'),
                        password=config.DATABASE.get('password'),
                        host=config.DATABASE.get('localhost'),
                        port=config.DATABASE.get('port'),
                        database_name=config.DATABASE.get('database_name'),
                        driver_name=config.DATABASE.get('driver_name'),
                        driver=config.DATABASE.get('driver'))
    """Create Empty Tables"""
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    session.commit()
    session.close()
