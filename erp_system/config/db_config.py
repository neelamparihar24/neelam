import mysql.connector
from mysql.connector import Error


class DBConfig:

    @staticmethod
    def get_connection():
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="neelam24",
                database="erp_system_python"
            )
            return connection
        except Error as e:
            print("Database Connection Error:", e)