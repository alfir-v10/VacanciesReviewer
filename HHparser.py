# https://dev.hh.ru/
import requests
import config


class VacancyInfoBySearchPage:
    def __init__(self, vacancy):
        self.vacancy_id = self.getByKeyFromObject(vacancy, 'id')  # str
        self.name = self.getByKeyFromObject(vacancy, 'name')  # str

        self.department = self.getByKeyFromObject(vacancy, 'department')  # dict
        self.department_id = self.getByKeyFromObject(self.department, 'id')  # str
        self.department_name = self.getByKeyFromObject(self.department, 'name')  # str

        self.has_test = self.getByKeyFromObject(vacancy, 'has_test')  # bool
        self.premium = self.getByKeyFromObject(vacancy, 'premium')  # bool
        self.archived = self.getByKeyFromObject(vacancy, 'archived')  # bool
        self.created_at = self.getByKeyFromObject(vacancy, 'created_at')  # str
        self.published_at = self.getByKeyFromObject(vacancy, 'published_at')  # str
        self.response_url = self.getByKeyFromObject(vacancy, 'response_url')  # str
        self.response_letter_required = self.getByKeyFromObject(vacancy, 'response_letter_required')  # bool
        self.url = self.getByKeyFromObject(vacancy, 'url')  # str
        self.sort_point_distanse = self.getByKeyFromObject(vacancy, 'sort_point_distanse')  # float

        self.working_days = self.getByKeyFromObject(vacancy, 'working_days')  # list of dicts
        self.working_time_intervals = self.getByKeyFromObject(vacancy, 'working_time_intervals')  # list of dicts
        self.working_time_modes = self.getByKeyFromObject(vacancy, 'working_time_modes')  # list of dicts

        self.address = self.getByKeyFromObject(vacancy, 'address')  # dict
        self.city = self.getByKeyFromObject(self.address, 'city')  # str
        self.street = self.getByKeyFromObject(self.address, 'street')  # str
        self.building = self.getByKeyFromObject(self.address, 'building')  # str
        self.address_description = self.getByKeyFromObject(self.address, 'description')  # str
        self.address_latitude = self.getByKeyFromObject(self.address, 'lat')  # float
        self.address_longitude = self.getByKeyFromObject(self.address, 'lng')  # float
        self.address_raw = self.getByKeyFromObject(self.address, 'raw')  # str

        self.metro = self.getByKeyFromObject(self.address, 'metro')  # dict
        self.station_id = self.getByKeyFromObject(self.metro, 'station_id')  # str
        self.station_name = self.getByKeyFromObject(self.metro, 'station_name')  # str
        self.line_id = self.getByKeyFromObject(self.metro, 'line_id')  # str
        self.line_name = self.getByKeyFromObject(self.metro, 'line_name')  # str
        self.station_latitude = self.getByKeyFromObject(self.metro, 'station_latitude')  # float
        self.station_longitude = self.getByKeyFromObject(self.metro, 'station_longitude')  # float
        self.metro_stations = self.getByKeyFromObject(vacancy, 'metro_stations')  # list of dicts

        self.type_vacancy = self.getByKeyFromObject(vacancy, 'type')  # dict
        self.type_id = self.getByKeyFromObject(self.type_vacancy, 'id')  # str
        self.type_name = self.getByKeyFromObject(self.type_vacancy, 'name')  # str

        self.area = self.getByKeyFromObject(vacancy, 'area')  # dict
        self.area_id = self.getByKeyFromObject(self.area, 'id')  # str
        self.area_name = self.getByKeyFromObject(self.area, 'name')  # str
        self.area_url = self.getByKeyFromObject(self.area, 'url')  # str

        self.contacts = self.getByKeyFromObject(vacancy, 'contacts')  # dict
        self.contact_name = self.getByKeyFromObject(self.contacts, 'name')  # str
        self.contacts_email = self.getByKeyFromObject(self.contacts, 'email')  # str
        self.contacts_phones = self.getByKeyFromObject(self.contacts, 'phones')  # list of dicts

        self.employer = self.getByKeyFromObject(vacancy, 'employer')  # dict
        self.employer_url = self.getByKeyFromObject(self.employer, 'url')  # str
        self.employer_id = self.getByKeyFromObject(self.employer, 'id')  # str
        self.employer_name = self.getByKeyFromObject(self.employer, 'name')  # str
        self.employer_trusted = self.getByKeyFromObject(self.employer, 'trusted')  # bool
        self.employer_vacancies_url = self.getByKeyFromObject(self.employer, 'vacancies_url')  # str

        self.salary = self.getByKeyFromObject(vacancy, 'salary')  # dict
        self.salary_to = self.getByKeyFromObject(self.salary, 'to')  # str
        self.salary_from = self.getByKeyFromObject(self.salary, 'from')  # str
        self.salary_currency = self.getByKeyFromObject(self.salary, 'currency')  # str
        self.salary_gross = self.getByKeyFromObject(self.salary, 'gross')  # bool

        self.schedule = self.getByKeyFromObject(vacancy, 'schedule')  # dict
        self.schedule_id = self.getByKeyFromObject(self.schedule, 'id')  # str
        self.schedule_name = self.getByKeyFromObject(self.schedule, 'name')  # str

        self.snippet = self.getByKeyFromObject(vacancy, 'snippet')  # dict
        self.snippet_requirements = self.getByKeyFromObject(self.snippet, 'requirement')  # str
        self.snippet_responsibility = self.getByKeyFromObject(self.snippet, 'responsibility')  # str

    @staticmethod
    def getByKeyFromObject(dictionary: dict, key: str):
        if dictionary:
            return dictionary.setdefault(key)


class VacancyInfoByVacancyPage(VacancyInfoBySearchPage):
    def __init__(self, vacancy):
        super().__init__(vacancy)
        self.vacancy = self.getVacancyById(vacancy_id=self.vacancy_id)

        self.billing_type = self.getByKeyFromObject(self.vacancy, 'billing_type')  # dict
        self.billing_type_id = self.getByKeyFromObject(self.billing_type, 'id')  # str
        self.billing_type_name = self.getByKeyFromObject(self.billing_type, 'name')  # str

        self.insider_interview = self.getByKeyFromObject(self.vacancy, 'insider_interview')  # dict
        self.insider_interview_id = self.getByKeyFromObject(self.insider_interview, 'id')  # str
        self.insider_interview_url = self.getByKeyFromObject(self.insider_interview, 'url')  # str

        self.allow_messages = self.getByKeyFromObject(self.vacancy, 'allow_messages')  # bool

        self.experience = self.getByKeyFromObject(self.vacancy, 'experience')  # dict
        self.experienceId = self.getByKeyFromObject(self.experience, 'id')  # str
        self.experienceName = self.getByKeyFromObject(self.experience, 'name')  # str

        self.employment = self.getByKeyFromObject(self.vacancy, 'employment')  # dict
        self.employmentId = self.getByKeyFromObject(self.employment, 'id')
        self.employmentName = self.getByKeyFromObject(self.employment, 'name')  # str

        self.vacancy_description = self.getByKeyFromObject(self.vacancy, 'description')
        self.key_skills = self.getByKeyFromObject(self.vacancy, 'key_skills')
        self.accept_handicapped = self.getByKeyFromObject(self.vacancy, 'accept_handicapped')  # bool
        self.accept_kids = self.getByKeyFromObject(self.vacancy, 'accept_kids')  # bool
        self.specializations = self.getByKeyFromObject(self.vacancy, 'specializations')
        self.professional_roles = self.getByKeyFromObject(self.vacancy, 'professional_roles')
        self.vacancy_code = self.getByKeyFromObject(self.vacancy, 'vacancy_code')
        self.hidden = self.getByKeyFromObject(self.vacancy, 'hidden')
        self.quick_responses_allowed = self.getByKeyFromObject(self.vacancy, 'quick_responses_allowed')
        self.driver_license_types = self.getByKeyFromObject(self.vacancy, 'driver_license_types')
        self.accept_incomplete_resumes = self.getByKeyFromObject(self.vacancy, 'accept_incomplete_resumes')  # bool
        self.accept_temporary = self.getByKeyFromObject(self.vacancy, 'accept_temporary')  # bool
        self.languages = self.getByKeyFromObject(self.vacancy, 'languages')  # list of dicts

    def getVacancyById(self, vacancy_id: int | None = None):
        if not vacancy_id:
            vacancy_id = self.vacancy_id
        url = f"{config.URL_HEADHUNTER}/vacancies/{vacancy_id}"
        req = requests.get(url)
        if req.status_code == 200:
            res = req.json()
            return res

    @staticmethod
    def getByKeyFromObject(dictionary: dict, key: str):
        if dictionary:
            return dictionary.setdefault(key)


class ProfessionalRole:
    def __init__(self, role):
        self.role = role  # dict
        self.role_id = self.getByKeyFromObject(role, 'id')  # str
        self.role_name = self.getByKeyFromObject(role, 'name')  # str

    @staticmethod
    def getByKeyFromObject(dictionary: dict, key: str):
        if dictionary:
            return dictionary.setdefault(key)


class Working:
    def __init__(self, work):
        """use it for working_days, working_time_intervals, working_time_modes"""
        self.work = work  # dict
        self.work_id = self.getByKeyFromObject(work, 'id')  # str
        self.work_name = self.getByKeyFromObject(work, 'name')  # str

    @staticmethod
    def getByKeyFromObject(dictionary: dict, key: str):
        if dictionary:
            return dictionary.setdefault(key)


class Language:
    def __init__(self, language):
        self.language = language  # dict
        self.language_id = self.getByKeyFromObject(self.language, 'id')  # str
        self.language_name = self.getByKeyFromObject(self.language, 'name')  # str
        self.language_level = self.getByKeyFromObject(self.language, 'level')  # str
        self.language_level_id = self.getByKeyFromObject(self.language_level, 'id')  # str
        self.language_level_name = self.getByKeyFromObject(self.language_level, 'name')  # str

    @staticmethod
    def getByKeyFromObject(dictionary: dict, key: str):
        if dictionary:
            return dictionary.setdefault(key)


class Specialization:
    def __init__(self, specialization):
        self.specialization = specialization  # dict
        self.id = self.getByKeyFromObject(self.specialization, 'id') # str
        self.name = self.getByKeyFromObject(self.specialization, 'name') # str
        self.profarea_id = self.getByKeyFromObject(self.specialization, 'profarea_id') # str
        self.profarea_name = self.getByKeyFromObject(self.specialization, 'profarea_name') # str

    @staticmethod
    def getByKeyFromObject(dictionary: dict, key: str):
        if dictionary:
            return dictionary.setdefault(key)


class Metro:
    def __init__(self, metro_station):
        self.station = metro_station  # dict
        self.station_id = self.getByKeyFromObject(self.station, 'station_id')  # str
        self.station_name = self.getByKeyFromObject(self.station, 'station_name')  # str
        self.line_id = self.getByKeyFromObject(self.station, 'line_id')  # str
        self.line_name = self.getByKeyFromObject(self.station, 'line_name')  # str
        self.station_latitude = self.getByKeyFromObject(self.station, 'station_latitude')  # float
        self.station_longitude = self.getByKeyFromObject(self.station, 'station_longitude')  # float

    @staticmethod
    def getByKeyFromObject(dictionary: dict, key: str):
        if dictionary:
            return dictionary.setdefault(key)


class Contacts:
    def __init__(self, contact):
        self.contact = contact  # dict
        self.country = self.getByKeyFromObject(self.contact, 'country')  # str
        self.city = self.getByKeyFromObject(self.contact, 'city')  # str
        self.number = self.getByKeyFromObject(self.contact, 'number')  # str
        self.comment = self.getByKeyFromObject(self.contact, 'comment')  # str

    @staticmethod
    def getByKeyFromObject(dictionary: dict, key: str):
        if dictionary:
            return dictionary.setdefault(key)


def getVacancies(text, page=0, per_page=100):
    url = f"{config.URL_HEADHUNTER}/vacancies?text='{text}'&page={page}&per_page={per_page}"
    print(url)
    req = requests.get(url)
    if req.status_code == 200:
        res = req.json()
        return res


if __name__ == '__main__':
    text = 'data science'
    data = getVacancies(text, per_page=5)
    items = data['items']
    for item in items:
        vacancy = VacancyInfoByVacancyPage(vacancy=item)
