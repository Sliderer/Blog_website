import sqlite3
from models import UserLogin, Blog


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
        if not return_result:
            return None
        else:
            return_result = return_result[0]

        result_user = UserLogin().init_from_tuple(return_result)
        return result_user

    def __find_user(self, criteria: str, value: str) -> UserLogin:
        command = f"SELECT * FROM users WHERE {criteria}={value}"
        return_result = self.__execute_command(command)
        if not return_result:
            return None
        else:
            return_result = return_result[0]

        result_user = UserLogin().init_from_tuple(return_result)
        return result_user

    def find_user_by_id(self, user_id) -> UserLogin:
        return self.__find_user('id', user_id)

    def find_user_by_email(self, email) -> UserLogin:
        return self.__find_user('email', f"'{email}'")

    def get_user_blogs(self, user: UserLogin):
        command = f"SELECT * FROM blogs WHERE user_id='{user.id}'"
        blogs = self.__execute_command(command)
        blogs = [Blog().init_from_tuple(data) for data in blogs]
        return blogs

    def add_user_blog(self, used_id: int, blog: Blog):
        command = f"INSERT INTO blogs VALUES (NULL, {used_id}, '{blog.title}', '{blog.text}')"
        self.__execute_command(command)

    def find_blog_by_id(self, blog_id: int) -> Blog:
        command = f"SELECT * FROM blogs WHERE id={blog_id}"
        result = self.__execute_command(command)
        blog = Blog().init_from_tuple(result[0])
        return blog


