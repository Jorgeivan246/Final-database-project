import mysql.connector
from mysql.connector import Error


# Se hace la conexion a la base de datos
class DAO:

    def __init__(self):

        self.connection = mysql.connector.connect(
            host='localhost',
            port=3306,
            user='root',
            db='proyecto_bases'
        )

        self.cursor = self.connection.cursor()

        print("Conexion establecida exitosamente")

    # Metodo para listar los datos de una entidad
    def listar(self, entidadAUsar):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                cursor.execute("SELECT * FROM " + entidadAUsar)
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    # Metodo para registrar una recepcion
    def registrarRecepcion(self, recepcion):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql = "INSERT INTO Recepcion (codigo, fecha, totalUnidades, Apicultor_Persona_cedula, Apicultor_Persona_email, Conductor_Persona_cedula, Conductor_Persona_email, Lote_codigo) VALUES ({0}, {1}, {2}, {3}, '{4}', {5}, '{6}', {7})"
                cursor.execute(
                    sql.format(recepcion[0], recepcion[1], recepcion[2], recepcion[3], recepcion[4], recepcion[5],
                               recepcion[6], recepcion[7]))
                self.connection.commit()
                print("¡Recepcion registrada!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    # Metodo para actualizar una recepcion
    def actualizarRecepcion(self, recepcion):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql = "UPDATE Recepcion SET fecha = {0}, totalUnidades = {1}, Apicultor_Persona_cedula = {2}, Apicultor_Persona_email = '{3}', Conductor_Persona_cedula = {4}, Conductor_Persona_email = '{5}', Lote_codigo = {6} WHERE codigo = {7}"
                cursor.execute(
                    sql.format(recepcion[1], recepcion[2], recepcion[3], recepcion[4], recepcion[5], recepcion[6],
                               recepcion[7], recepcion[0]))
                self.connection.commit()
                print("¡Recepcion actualizada!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    # Metodo para eliminar una recepcion
    def eliminarRecepcion(self, codigoRecepcionEliminar):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql = "DELETE FROM Recepcion WHERE codigo = '{0}'"
                cursor.execute(sql.format(codigoRecepcionEliminar))
                self.connection.commit()
                print("¡Recepcion eliminada!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    # Metodo para registrar un producto
    def registrarProducto(self, producto):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql = "insert into producto (idProducto, fecha, peso_neto, peso_bruto, Recepcion_codigo, Recepcion_fecha, Tipo_Producto_idTipo) VALUE({0},{1}, {2}, {3},{4}, {5}, {6})"
                cursor.execute(sql.format(producto[0], producto[1], producto[2], producto[3], producto[4], producto[5],
                                          producto[6]))
                self.connection.commit()
                print("¡Producto registrado!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    # Metodo para actualizar un producto
    def actualizarProducto(self, producto):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql = "UPDATE producto SET fecha = {0}, peso_neto = {1}, peso_bruto = {2}, Recepcion_codigo = {3}, " \
                      "Recepcion_fecha = {4}, Tipo_Producto_idTipo = {5} WHERE idProducto = {6}"
                cursor.execute(sql.format(producto[1], producto[2], producto[3], producto[4], producto[5], producto[6],
                                          producto[0]))
                self.connection.commit()
                print("producto actualizado!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    # Metodo para eliminar un producto
    def eliminarProducto(self, codigoCursoEliminar):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql = "DELETE FROM producto WHERE idProducto = {0}"
                cursor.execute(sql.format(codigoCursoEliminar))
                self.connection.commit()
                print("¡Producto eliminado!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    # Metodo para registrar un envasado
    def registrarEnvasado(self, envasado):
        if self.connection.is_connected():
            cursor = self.connection.cursor()
            sql = "INSERT INTO envasado (codigo, fecha, Lote_codigo,Muestreo_codigo) VALUES ({0}, {1}, {2}, {3})"
            cursor.execute(sql.format(envasado[0], envasado[1], envasado[2], envasado[3]))
            self.connection.commit()
            print("¡Curso registrado!\n")

    # Metodo para actualizar un envasado
    def actualizarEnvasado(self, envasado):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql = "UPDATE envasado SET fecha = {1},lote_codigo = {2},muestreo_codigo ={3} WHERE codigo = {0}"
                cursor.execute(sql.format(envasado[0], envasado[1], envasado[2], envasado[3]))
                self.connection.commit()
                print("¡Envasado actualizado!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    # Metodo para eliminar un envasado
    def eliminarEnvasado(self, codigoEnvasadoEliminar):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql = "DELETE FROM envasado WHERE codigo = {0}"
                cursor.execute(sql.format(codigoEnvasadoEliminar))
                self.connection.commit()
                print("¡Envasado eliminado!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))
