


DATABASE_PATH = 'data_store/db/py_ano.db'


class AppConfig:
    def __init__(self, db_path: str = DATABASE_PATH):
        self.db_path = db_path

    # TODO Kreirati metodu koja ce se pokrenuti u kontruktoru
    # i iz config.yaml datoteke ucitati putanje i ostale inicijalne postavke
