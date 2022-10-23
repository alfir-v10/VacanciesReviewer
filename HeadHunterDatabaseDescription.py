import config
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Vacancy(Base):
    __tablename__ = 'vacancies'
    id = Column(Integer, primary_key=True, autoincrement=True)
    vacancy_id = Column(String, unique=True)
    name = Column(String)
    created_at = Column(String)
    published_at = Column(String)
    sort_point_distanse = Column(String)
    snippet_requirements = Column(String)
    snippet_responsibility = Column(String)
    vacancy_description = Column(String)
    vacancy_code = Column(String)
    url = Column(String)
    response_url = Column(String)

    has_test = Column(Boolean)
    premium = Column(Boolean)
    archived = Column(Boolean)
    allow_messages = Column(Boolean)
    response_letter_required = Column(Boolean)
    accept_handicapped = Column(Boolean)
    accept_kids = Column(Boolean)
    hidden = Column(Boolean)
    accept_incomplete_resumes = Column(Boolean)
    accept_temporary = Column(Boolean)
    quick_responses_allowed = Column(Boolean)

    department_id = Column(Integer, ForeignKey('department.id'))
    type_id = Column(Integer, ForeignKey('type_vacancy.id'))
    area_id = Column(Integer, ForeignKey('area.id'))
    station_id = Column(Integer, ForeignKey('metro.id'))
    employer_id = Column(Integer, ForeignKey('employer.id'))
    employment_id = Column(Integer, ForeignKey('employment.id'))
    schedule_id = Column(Integer, ForeignKey('schedule.id'))
    billing_type_id = Column(Integer, ForeignKey('billing_type.id'))
    experience_id = Column(Integer, ForeignKey('experience.id'))
    insider_interview_id = Column(Integer, ForeignKey('insider_interview.id'))


class Languages(Base):
    __tablename__ = 'languages'
    id = Column(Integer, primary_key=True, autoincrement=True)
    vacancy_id = Column(Integer, ForeignKey('vacancies.id'))
    language_id = Column(Integer, ForeignKey('languages_name.id'))
    language_level_id = Column(Integer, ForeignKey('languages_level.id'))


class LanguagesName(Base):
    __tablename__ = 'languages_name'
    id = Column(Integer, primary_key=True, autoincrement=True)
    language_id = Column(String, unique=True)
    language_name = Column(String)


class LanguagesLevel(Base):
    __tablename__ = 'languages_level'
    id = Column(Integer, primary_key=True, autoincrement=True)
    language_level_id = Column(String, unique=True)
    language_level_name = Column(String)


class DriverLicenseTypes(Base):
    __tablename__ = 'driver_license_types'
    id = Column(Integer, primary_key=True, autoincrement=True)
    vacancy_id = Column(Integer, ForeignKey('vacancies.id'))
    license_id = Column(String)


class Specializations(Base):
    __tablename__ = 'specializations'
    id = Column(Integer, primary_key=True, autoincrement=True)
    vacancy_id = Column(Integer, ForeignKey('vacancies.id'))
    name = Column(Integer, ForeignKey('specializations_name.id'))
    profarea_id = Column(Integer, ForeignKey('profarea.id'))


class SpecializationsName(Base):
    __tablename__ = 'specializations_name'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True)


class ProfArea(Base):
    __tablename__ = 'profarea'
    id = Column(Integer, primary_key=True, autoincrement=True)
    profarea_id = Column(String, unique=True)
    profarea_name = Column(String)


class ProfessionalRoles(Base):
    __tablename__ = 'professional_roles'
    id = Column(Integer, primary_key=True, autoincrement=True)
    vacancy_id = Column(Integer, ForeignKey('vacancies.id'))
    role_id = Column(Integer, ForeignKey('roles.id'))


class Roles(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True, autoincrement=True)
    role_id = Column(String, unique=True)
    role_name = Column(String)


class KeySkills(Base):
    __tablename__ = 'key_skills'
    id = Column(Integer, primary_key=True, autoincrement=True)
    vacancy_id = Column(Integer, ForeignKey('vacancies.id'))
    skill = Column(Integer, ForeignKey('skills.id'))


class Skills(Base):
    __tablename__ = 'skills'
    id = Column(Integer, primary_key=True, autoincrement=True)
    skill = Column(String, unique=True)


class Employment(Base):
    __tablename__ = 'employment'
    id = Column(Integer, primary_key=True, autoincrement=True)
    employment_id = Column(String, unique=True)
    employment_name = Column(String)


class Experience(Base):
    __tablename__ = 'experience'
    id = Column(Integer, primary_key=True, autoincrement=True)
    experience_id = Column(String, unique=True)
    experience_name = Column(String)


class InsiderInterview(Base):
    __tablename__ = 'insider_interview'
    id = Column(Integer, primary_key=True, autoincrement=True)
    insider_interview_id = Column(String, unique=True)
    insider_interview_url = Column(String)


class BillingType(Base):
    __tablename__ = 'billing_type'
    id = Column(Integer, primary_key=True, autoincrement=True)
    billing_type_id = Column(String, unique=True)
    billing_type_name = Column(String)


class Schedule(Base):
    __tablename__ = 'schedule'
    id = Column(Integer, primary_key=True, autoincrement=True)
    schedule_id = Column(String, unique=True)
    schedule_name = Column(String)


class Salary(Base):
    __tablename__ = 'salary'
    id = Column(Integer, primary_key=True)
    vacancy_id = Column(Integer, ForeignKey('vacancies.id'))
    salary_to = Column(String)
    salary_from = Column(String)
    salary_currency = Column(String)
    salary_gross = Column(Boolean)


class Employer(Base):
    __tablename__ = 'employer'
    id = Column(Integer, primary_key=True, autoincrement=True)
    employer_id = Column(String, unique=True)
    employer_name = Column(String)
    employer_trusted = Column(String)
    employer_url = Column(String)
    employer_vacancies_url = Column(String)


class Contacts(Base):
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True)
    vacancy_id = Column(Integer, ForeignKey('vacancies.id'))
    contact_name = Column(String)
    contacts_email = Column(String)


class Phones(Base):
    __tablename__ = 'phones'
    id = Column(Integer, primary_key=True)
    vacancy_id = Column(Integer, ForeignKey('vacancies.id'))
    country = Column(String)
    city = Column(String)
    number = Column(String)
    comment = Column(String)


class Area(Base):
    __tablename__ = 'area'
    id = Column(Integer, primary_key=True, autoincrement=True)
    area_id = Column(String, unique=True)
    area_name = Column(String)
    area_url = Column(String)


class TypeVacancy(Base):
    __tablename__ = 'type_vacancy'
    id = Column(Integer, primary_key=True, autoincrement=True)
    type_id = Column(String, unique=True)
    type_name = Column(String)


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    vacancy_id = Column(Integer, ForeignKey('vacancies.id'))
    city = Column(String)
    street = Column(String)
    building = Column(String)
    address_description = Column(String)
    address_latitude = Column(Float)
    address_longitude = Column(Float)
    address_raw = Column(String)


class Metro(Base):
    __tablename__ = 'metro'
    id = Column(Integer, primary_key=True, autoincrement=True)
    station_id = Column(String, unique=True)
    station_name = Column(String)
    line_id = Column(String)
    line_name = Column(String)
    station_latitude = Column(Float)
    station_longitude = Column(Float)


class MetroStations(Base):
    __tablename__ = 'metro_stations'
    id = Column(Integer, primary_key=True)
    vacancy_id = Column(Integer, ForeignKey('vacancies.id'))
    station_id = Column(Integer, ForeignKey('metro.id'))
    station_name = Column(String)
    line_id = Column(String)
    line_name = Column(String)
    station_latitude = Column(String)
    station_longitude = Column(String)


class Department(Base):
    __tablename__ = 'department'
    id = Column(Integer, primary_key=True, autoincrement=True)
    department_id = Column(String, unique=True)
    department_name = Column(String)


class WorkingDays(Base):
    __tablename__ = 'working_days'
    id = Column(Integer, primary_key=True)
    vacancy_id = Column(Integer, ForeignKey('vacancies.id'))
    day_id = Column(String)
    day_name = Column(String)


class WorkingTimeIntervals(Base):
    __tablename__ = 'working_time_intervals'
    id = Column(Integer, primary_key=True)
    vacancy_id = Column(Integer, ForeignKey('vacancies.id'))
    interval_id = Column(String)
    interval_name = Column(String)


class WorkingTimeModes(Base):
    __tablename__ = 'working_time_modes'
    id = Column(Integer, primary_key=True)
    vacancy_id = Column(Integer, ForeignKey('vacancies.id'))
    mode_id = Column(String)
    mode_name = Column(String)


if __name__ == "__main__":
    from sqlalchemy.orm import sessionmaker
    from utils import get_engine

    engine = get_engine(user=config.DATABASE.get('user'),
                        password=config.DATABASE.get('password'),
                        host=config.DATABASE.get('host'),
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
