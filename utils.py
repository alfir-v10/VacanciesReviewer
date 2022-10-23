from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import config
import requests
import json
from types import SimpleNamespace
import datetime


def get_engine(user, password, host, port, database_name, driver_name, driver):
    url = f"{driver_name}+{driver}://{user}:{password}@{host}:{port}/{database_name}"
    engine = create_engine(url, echo=False)
    # print(engine.url)
    if not database_exists(engine.url):
        create_database(engine.url)
    return engine


def getVacanciesLikeObject(text, page=0, per_page=100, date_from=None, date_to=None):
    url = f"{config.URL_HEADHUNTER}/vacancies?text='{text}'&page={page}&per_page={per_page}"
    if date_from:
        url += f'&date_from={date_from}'
    if date_to:
        url += f'&date_to={date_to}'
    print(url)
    req = requests.get(url)
    if req.status_code == 200:
        return json.loads(req.text, object_hook=lambda d: SimpleNamespace(**d))


def getVacanciesLikeJson(text, page=0, per_page=100, date_from=None, date_to=None):
    url = f"{config.URL_HEADHUNTER}/vacancies?text='{text}'&page={page}&per_page={per_page}"
    if date_from:
        url += f'&date_from={date_from}'
    if date_to:
        url += f'&date_to={date_to}'
    # print(url)
    req = requests.get(url)
    if req.status_code == 200:
        return req.json()


def getTimeInterval(date_from, date_to, weeks=0, days=0, hours=0, minutes=0, seconds=0):
    date_from = datetime.datetime.strptime(date_from, '%Y-%m-%dT%H:%M:%S')
    date_to = datetime.datetime.strptime(date_to, '%Y-%m-%dT%H:%M:%S')
    intervals = []
    if any([weeks, days, hours, minutes, seconds]) and date_from < date_to:
        while date_from < date_to:
            new_date = date_from + datetime.timedelta(days=days, hours=hours,minutes=minutes, seconds=seconds)
            if new_date > date_to:
                new_date = date_to
            intervals.append((date_from.strftime('%Y-%m-%dT%H:%M:%S'), new_date.strftime('%Y-%m-%dT%H:%M:%S')))
            date_from = new_date
    return intervals

if __name__ == "__main__":
    date_from = '2022-09-01T00:00:00'
    date_to = '2022-10-01T00:00:00'
    intervals = getTimeInterval(date_from, date_to, weeks=0, days=5, hours=5, minutes=0, seconds=0)
    for date_to, date_from in intervals:
        print(date_to, date_from)