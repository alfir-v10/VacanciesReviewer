from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import config
import requests

def get_engine(user, password, host, port, database_name, driver_name, driver):
    url = f"{driver_name}+{driver}://{user}:{password}@{host}:{port}/{database_name}"
    engine = create_engine(url, echo=True)
    print(engine.url)
    if not database_exists(engine.url):
        create_database(engine.url)
    return engine

def getVacancies(text, page=0, per_page=100):
    url = f"{config.URL_HEADHUNTER}/vacancies?text='{text}'&page={page}&per_page={per_page}"
    print(url)
    req = requests.get(url)
    if req.status_code == 200:
        res = req.json()
        return res

if __name__ == "__main__":
    pass
