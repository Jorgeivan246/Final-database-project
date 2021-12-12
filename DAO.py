import mysql.connector
from mysql.connector import Error


#Se hace la conexion a la base de datos
class DAO():
   
        def  __init__(self):

            self.connection = mysql.connector.connect(
                     host='localhost',
                     port=3306,
                     user='root',
                     password='4600',
                     db='proyecto_bases'
                    )
                
               
            self.cursor = self.connection.cursor()

            print("Conexion establecida exitosamente")

        def listar(self,entidadAUsar):
            if self.connection.is_connected():
                try:
                    cursor = self.connection.cursor()
                    cursor.execute("SELECT * FROM " + entidadAUsar)
                    resultados = cursor.fetchall()
                    return resultados
                except Error as ex:
                    print("Error al intentar la conexión: {0}".format(ex))


        def registrar(self, curso):
            if self.connection.is_connected():
                try:
                    cursor = self.connection.cursor()
                    sql = "INSERT INTO curso (codigo, nombre, creditos) VALUES ('{0}', '{1}', {2})"
                    cursor.execute(sql.format(curso[0], curso[1], curso[2]))
                    self.connection.commit()
                    print("¡Curso registrado!\n")
                except Error as ex:
                    print("Error al intentar la conexión: {0}".format(ex))



        def registrarProducto(self, producto):
            if self.connection.is_connected():
                try:
                    cursor = self.conexion.cursor()
                    sql = "INSERT INTO producto (idProducto, fecha, peso_neto, peso_bruto, Recepcion_codigo, Recepcion_fecha, Tipo_Producto_idTipo) " \
                          "VALUES ('{0}','{1}', '{2}', '{3}','{4}', '{5}', '{6}')"
                    cursor.execute(sql.format(producto[0], producto[1], producto[2], producto[3], producto[4], producto[5], producto[6]))
                    self.conexion.commit()
                    print("producto registrado!\n")
                except Error as ex:
                    print("Error al intentar la conexión: {0}".format(ex))

        def actualizar(self, curso):
            if self.conexion.is_connected():
                try:
                    cursor = self.conexion.cursor
                    sql = "UPDATE curso SET nombre = '{0}', creditos = {1} WHERE codigo = '{2}'"
                    cursor.execute(sql.format(curso[1], curso[2], curso[0]))
                    self.conexion.commit()
                    print("¡Curso actualizado!\n")
                except Error as ex:
                    print("Error al intentar la conexión: {0}".format(ex))

        def eliminar(self, codigoCursoEliminar):
            if self.conexion.is_connected():
                try:
                    cursor = self.conexion.cursor()
                    sql = "DELETE FROM curso WHERE codigo = '{0}'"
                    cursor.execute(sql.format(codigoCursoEliminar))
                    self.conexion.commit()
                    print("¡Curso eliminado!\n")
                except Error as ex:
                    print("Error al intentar la conexión: {0}".format(ex))
                        
            