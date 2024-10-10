import sqlite3

class Database:
    def __init__(self, db_path="../../main.db"):
        self.db_path = db_path

    @property
    def connection(self):
        return sqlite3.connect(self.db_path)

    def execute(self, sql: str,
                parameters: tuple = None,
                fetchone = False,
                fetchall = False,
                commit = False ):
        if not parameters:
            parameters = ()
        connection = self.connection
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_user_table(self):
        sql = """CREATE TABLE IF NOT EXISTS Users (
                id INT PRIMARY KEY,
                name VARCHAR NOT NULL,
                phone VARCHAR,
                age INT,
                course VARCHAR
        )"""
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])

        return sql, tuple(parameters.values())

    def select_user(self, id):
        sql = "SELECT * FROM Users WHERE id = ?"
        parameters = (id,)
        # sql, parameters = self.format_args(sql, id)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def new_user(self, id, name, phone, age, course):
        self.create_user_table()
        if not self.select_user(id):
            sql = "INSERT INTO Users (id, name, phone, age, course) VALUES (?, ?, ?, ?, ?)"
            parameters = (id, name, phone, age, course)
            return self.execute(sql, parameters=parameters, commit=True)

    def count_users(self):
        sql = "SELECT COUNT(id) FROM Users"
        return self.execute(sql, fetchone=True)

    def users_list(self):
        sql = "SELECT * FROM Users"
        return self.execute(sql)
