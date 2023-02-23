import sqlite3
from models import UserLogin


class Database:
    __connection_string = 'website.db'

    def __execute_command(self, command: str):
        with sqlite3.connect(self.__connection_string) as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            result = cursor.fetchall()
        print(result)
        return result

    def add_user(self, user: UserLogin) -> UserLogin:
        command = f"INSERT INTO users VALUES (NULL, '{user.name}', '{user.password}', '{user.email}') RETURNING *"
        return_result = self.__execute_command(command)[0]
        result_user = UserLogin().init_from_tuple(return_result)
        return result_user

    def __find_user(self, criteria: str, value: str) -> UserLogin:
        command = f"SELECT * FROM users WHERE {criteria}={value}"
        return_result = self.__execute_command(command)[0]
        result_user = UserLogin().init_from_tuple(return_result)
        return result_user

    def find_user_by_id(self, user_id) -> UserLogin:
        return self.__find_user('id', user_id)

    def find_user_by_email(self, email) -> UserLogin:
        return self.__find_user('email', f"'{email}'")

