from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database


def get_engine(user, password, host, port, database_name, driver_name, driver):
    url = f"{driver_name}+{driver}://{user}:{password}@{host}:{port}/{database_name}"
    engine = create_engine(url, echo=True)
    print(engine.url)
    if not database_exists(engine.url):
        create_database(engine.url)
    return engine


if __name__ == "__main__":
    pass
