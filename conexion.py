import mysql.connector

class Database:
    def _init_(self):
        self.connection = pymysql.connect(
            user="root", 
            password="1234",database="proyecto_bases",
            port = "3306")

        self.cursor = self.connection.cursor()

        print("Conexion establecida exitosamente")
database = Database()
