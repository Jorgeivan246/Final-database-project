import mysql.connector
from mysql.connector import Error
from generar_graficas import Grafica 


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
    
    # Metodo para registrar un muestreo
    def registrarMuestreo(self, muestreo):
        if self.connection.is_connected():
            cursor = self.connection.cursor()
            sql = "INSERT INTO muestreo (codigo, fecha, unidades_aceptadas, Empleado_Persona_cedula, Empleado_Persona_email) VALUES ({0}, {1}, {2}, {3}, '{4}')"
            cursor.execute(sql.format(muestreo[0], muestreo[1], muestreo[2], muestreo[3], muestreo[4]))
            self.connection.commit()
            print("¡Muestreo registrado!\n")

    # Metodo para actualizar un muestreo
    def actualizarMuestreo(self, muestreo):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql = "UPDATE muestreo SET fecha = {1},unidades_aceptadas = {2},Empleado_Persona_cedula ={3},Empleado_Persona_email ='{4}' WHERE codigo = {0}"
                cursor.execute(sql.format(muestreo[0], muestreo[1], muestreo[2], muestreo[3], muestreo[4]))
                self.connection.commit()
                print("¡Muestreo actualizado!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    # Metodo para eliminar un muestreo
    def eliminarMuestreo(self, codigoMuestreoEliminar):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql = "DELETE FROM muestreo WHERE codigo = {0}"
                cursor.execute(sql.format(codigoMuestreoEliminar))
                self.connection.commit()
                print("¡Muestreo eliminado!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    # Metodo para validar el login
    def validarLogin(self, login):
        if self.connection.is_connected():
            cursor = self.connection.cursor()
            sql = "SELECT * FROM Empleado WHERE Cargo_codigo IN (1,2,5)"
            cursor.execute(sql)
            empleado = cursor.fetchall()
            for row in empleado:
                if login[0] == row[1] and login[1] == row[0]:
                    return True
            
            return False

    # Metodo para reprotar los empleados que ganan más de 800000
    def reporteEmpleados800(self):
        if self.connection.is_connected():
            cursor = self.connection.cursor()
            sql = "SELECT persona_cedula, salario FROM empleado e INNER JOIN cargo c  WHERE c.salario > 800000"
            cursor.execute(sql)
            empleados = cursor.fetchall()
            return empleados

    # Metodo para listar el promedio del peso neto de los productos por el tipo de producto
    def promedioPesoNetoPorTipo(self):
        if self.connection.is_connected():
            cursor = self.connection.cursor()
            sql = "SELECT Tipo_Producto_idTipo, ROUND (AVG(peso_neto),2) AS promedio FROM Producto GROUP BY(Tipo_Producto_idTipo)"
            cursor.execute(sql)
            promedioPesoNetoPorTipo = cursor.fetchall()
            return promedioPesoNetoPorTipo

    # Metodo para calcular la nomina de los gerentes
    def calcularNominasGerentes(self):
        if self.connection.is_connected():
            cursor = self.connection.cursor()
            sql = "SELECT SUM(salario) AS nomina FROM cargo c INNER JOIN empleado e ON c.codigo = e.cargo_codigo  WHERE c.descripcion = 'gerente' "
            cursor.execute(sql)
            nominaGerentes = cursor.fetchall()
            return nominaGerentes

    def consulta3(self):
        if self.connection.is_connected():
            cursor = self.connection.cursor()
            sql = "SELECT * FROM Producto WHERE peso_bruto BETWEEN 28 AND 32 AND fecha > DATE('2021-05-01')"
            cursor.execute(sql)
            resultados = cursor.fetchall()
            return resultados

    def consulta4(self):
        if self.connection.is_connected():
            cursor = self.connection.cursor()
            sql = "SELECT descripcion, SUM(peso_bruto) AS peso_total FROM tipo_producto  tp INNER JOIN producto p ON tp.idTipo = p.Tipo_Producto_idTipo GROUP BY (descripcion)"
            cursor.execute(sql)
            resultados = cursor.fetchall()
            return resultados

    def consultaPlantilla(self,sql):
        if self.connection.is_connected():
            cursor = self.connection.cursor()
            cursor.execute(sql)
            resultados = cursor.fetchall()
            return resultados

    def reporteo1(self):
        
        
        #Mostrar en un gráfica de barras el peso neto total de las 4 recepciones más recientes GRAFICO

        if self.connection.is_connected():
            
            cursor = self.connection.cursor()
            sql = "SELECT SUM(peso_neto) as total from Producto p NATURAL JOIN Recepcion r GROUP BY r.codigo limit 4"
            cursor.execute(sql)
            registros=cursor.fetchall()
        return registros
    
    def definirReportePdf1(self):
        
       
        registros=self.reporteo1()

        datos=[1,2,3,4,5]
        
        datos.extend(registros)
            
        grafica = Grafica()

        nombreImagen="graficoBarrasRecepcion"


        grafica.generarEstadisticaBarrasRecepcion(datos)
        grafica.generarPDf(nombreImagen)


    def reporte2(self):
        
        #El peso bruto total de los productos agrupados por el nombre del tipo producto
        
        if self.connection.is_connected():
            
            cursor = self.connection.cursor()
            sql = "SELECT SUM(peso_bruto) AS peso_total FROM tipo_producto  tp INNER JOIN producto p ON tp.idTipo = p.Tipo_Producto_idTipo GROUP BY (descripcion)"
            cursor.execute(sql)
            registros=cursor.fetchall()
          
        return registros
    
    def definirRegistroPdf2(self):
        
        registros=self.reporte2()

        datos=[1,2,3,4]

      

        datos.extend(registros)
            
        grafica = Grafica()

        nombreImagen="graficoPastelEnvasado"


        grafica.generarEstadisticaBarrasPastel(datos)
        grafica.generarPDf(nombreImagen)