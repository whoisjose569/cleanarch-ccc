from sqlalchemy import create_engine
from os import getenv

class DBConnectionHandler:

    def __init__(self) -> None:
        self.__connection_string = "{}://{}:{}@{}:{}/{}".format(
            'mysql+pymysql',
            'root',
            getenv('MYSQL_PASSWORD'),
            'localhost',
            '3306',
            'ccc_database'
        )
        self.__engine = self.__create_database_engine()
    
    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine
    
    def get_engine(self):
        return self.__engine