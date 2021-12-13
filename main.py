from DAO import DAO
import funciones
import string
import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def login():
    clearConsole()
    dao = DAO()
    print("==================== LOGIN ====================")
    login = funciones.pedirDatosLogin()
    
    if dao.validarLogin(login):
        print("Bienvenido")
        sub_menu()
    else:
        print("Email o contraseña incorrectos")
        login()

def sub_menu():
    clearConsole()
    entidadAUsar=""
    
    print("======== Elija la entidad que desea manipular ==========")
    print("1.- Recepcion ")
    print("2.- Envasado ")
    print("3.- Muestreo")
    print("4.- Producto")
    print("5.- Reportes")
    print("==================================")
    opcion = int(input("Seleccione una opción: "))
            
    if opcion == 1:
        entidadAUsar="Recepcion"
    elif opcion == 2:
        entidadAUsar="Envasado"
    elif opcion == 3:
        entidadAUsar="Muestreo"
    elif opcion == 4:
        entidadAUsar="Producto"
    elif opcion == 5:
        reportes() 
    else:
        print("Opción no válida...")
        sub_menu()
    menu_principal(entidadAUsar)
            
                    

def menu_principal(entidadAUsar: string):
    clearConsole()
    continuar = True
    while continuar:
        opcion_correcta = False
        while not opcion_correcta:
            print("==================== MENÚ PRINCIPAL ====================")
            print("1.- Listar "+ entidadAUsar)
            print("2.- Registrar " + entidadAUsar)
            print("3.- Actualizar " + entidadAUsar)
            print("4.- Eliminar " + entidadAUsar)
            print("5.- Salir")
            print("========================================================")
            opcion = int(input("Seleccione una opción: "))

            if opcion < 1 or opcion > 5:
                print("Opción incorrecta, ingrese nuevamente...")
            elif opcion == 5:
                continuar = False
                print("¡Gracias por usar este sistema!")
                break
            else:
                opcion_correcta = True
                ejecutarOpcion(opcion,entidadAUsar)


def opcionesRecpcion(opcion: int,entidadAUsar: string):
    clearConsole()
    dao = DAO()
    recepciones = dao.listar(entidadAUsar)
         
    if opcion == 1:
        funciones.listarRecepciones(recepciones)
    elif opcion == 2:
        dao.registrarRecepcion(funciones.pedirDatosRegistroRecepcion())
    elif opcion == 3:
        dao.actualizarRecepcion(funciones.pedirDatosActualizacionRecepcion(recepciones))
    elif opcion == 4:
        dao.eliminarRecepcion(funciones.pedirDatosEliminarRecepcion(recepciones))
    else:
        print("Opción no válida...")

        
def opcionesProducto(opcion: int,entidadAUsar: string):
    clearConsole()
    dao = DAO()
    productos = dao.listar(entidadAUsar)
         
    if opcion == 1:
        funciones.listarProductos(productos)
    elif opcion == 2:
        dao.registrarProducto(funciones.pedirDatosRegistroProducto())
    elif opcion == 3:
        dao.actualizarProducto(funciones.pedirDatosActualizacionProducto(productos))
    elif opcion == 4:
        dao.eliminarProducto(funciones.pedirDatosEliminarProducto(productos))
    else:
        print("Opción no válida...")

def opcionesEnvasado(opcion: int,entidadAUsar: string):
    clearConsole()
    dao = DAO()
    envasados = dao.listar(entidadAUsar)
         
    if opcion == 1:
        funciones.listarEnvasados(envasados)
    elif opcion == 2:
        dao.registrarEnvasado(funciones.pedirDatosRegistroEnvasado())
    elif opcion == 3:
        dao.actualizarEnvasado(funciones.pedirDatosActualizacionEnvasado(envasados))
    elif opcion == 4:
        dao.eliminarEnvasado(funciones.pedirDatosEliminarEnvasado(envasados))
    else:
        print("Opción no válida...")

def opcionesMuestreo(opcion: int,entidadAUsar: string):
    clearConsole()
    dao = DAO()
    muestreos = dao.listar(entidadAUsar)
         
    if opcion == 1:
        funciones.listarMuestreos(muestreos)
    elif opcion == 2:
        dao.registrarMuestreo(funciones.pedirDatosRegistroMuestreo())
    elif opcion == 3:
        dao.actualizarMuestreo(funciones.pedirDatosActualizacionMuestreo(muestreos))
    elif opcion == 4:
        dao.eliminarMuestreo(funciones.pedirDatosEliminarMuestreo(muestreos))
    else:
        print("Opción no válida...")

def ejecutarOpcion(opcion: int,entidadAUsar: string):
    clearConsole()

    if entidadAUsar == "Recepcion":
        opcionesRecpcion(opcion,entidadAUsar)
    elif entidadAUsar == "Envasado":
        opcionesEnvasado(opcion,entidadAUsar)
    elif entidadAUsar == "Muestreo":
        opcionesMuestreo(opcion,entidadAUsar)
    elif entidadAUsar == "Producto":
        opcionesProducto(opcion,entidadAUsar)
    elif entidadAUsar == "Reportes":
        reportes(opcion)
    else:
        ("Entidad no válida...")

def reportes():
    decision = True
    while decision:
        clearConsole()
        print("==================== REPORTES ====================")
        print("1. Listar los empleados que tengan un sueldo mayor o igual a 800000")
        print("2. Listar el promedio del peso neto de los productos por el tipo de producto ")
        print("3. Listar todos los productos en donde el peso bruto esté entre 32 kilos y 28 kilos y que su fecha fecha sea mayor a 2021-05-01")
        print("4. El peso bruto total de los productos agrupados por el nombre del tipo producto")
        print("5. Mostrar la Nómina de los empleados que tengan el cargo de “gerente” ")
        print("6. Mostrar la placa y fecha de los vehículos en los cuales su modelo es mayor a 2019 ordenar del más antiguo al más nuevo")
        print("7. Mostrar en un gráfica de barras el peso neto total de las 4 recepciones más recientes")
        print("8. listar el id  de los empleados que tengan un nivel académico de bachiller, doctorado o magíster, o  aquellos que tengan Cargo de gerente, auxiliar de calidad o jefe de planta.")
        print("9. Listar los conductores cuya licencia expira en el año 2022, listar sólo aquellos que      tengan su autorización activa.")
        print("10. Nos faltó por implementar esta opción")
        print("11. Salir")

        opcion = int(input("Seleccione una opción: "))

        dao = DAO()
        if opcion == 1:
            sueldos = dao.consultaPlantilla("SELECT persona_cedula, salario FROM empleado e INNER JOIN cargo c  WHERE c.salario > 800000")
            funciones.generarReporte1(sueldos)
        elif opcion == 2:
            promedios = dao.consultaPlantilla("SELECT Tipo_Producto_idTipo, AVG(peso_neto) AS promedio FROM Producto GROUP BY(Tipo_Producto_idTipo)")
            funciones.generarReporte2(promedios)
        elif opcion == 3:
            resultados = dao.consultaPlantilla("SELECT * FROM Producto WHERE peso_bruto BETWEEN 28 AND 32 AND fecha > DATE('2021-05-01')")
            funciones.generarReporte3(resultados)
        elif opcion == 4:
            dao.definirRegistroPdf2()
        elif opcion == 5:
            nominasGerentes = dao.consultaPlantilla("SELECT SUM(salario) AS nomina FROM cargo  c INNER JOIN empleado e ON c.codigo = e.cargo_codigo  WHERE c.descripcion= 'gerente'")
            funciones.generarReporte5(nominasGerentes)
        elif opcion == 6:
            resultados = dao.consultaPlantilla("SELECT placa, fecha_modelo FROM vehiculo v INNER JOIN modelo m on v.modelo_codigo = m.codigo WHERE fecha_modelo>DATE('2009-01-01') group by placa order by fecha_modelo")
            funciones.generarReporte6(resultados)
        elif opcion == 7:
            dao.definirReportePdf1()
        elif opcion == 8:
            resultados = dao.consultaPlantilla("SELECT persona_cedula From empleado e INNER JOIN cargo c ON e.cargo_codigo = c.codigo INNER JOIN nivel_academico n ON e.nivel_academico_codigo= n.codigo  WHERE (n.descripcion = 'gerente' or  n.descripcion = 'auxiliar de calidad' or n.descripcion = 'jefe de planta') OR (n.descripcion = 'Bachiller' or n.descripcion = 'Doctorado' or n.descripcion = 'Magíster')")
            funciones.generarReporte8(resultados)
        elif opcion == 9:
            resultados = dao.consultaPlantilla("SELECT persona_cedula FROM conductor c INNER JOIN licencia l ON c.licencia_codigo_licencia = l.codigo_licencia WHERE l.fecha_vencimiento >=DATE('2022-01-01') AND l.fecha_vencimiento <=DATE('2022-12-31') GROUP BY persona_cedula")
            funciones.generarReporte9(resultados)
        elif opcion == 10:
            print("Nos falta implementar esta opción")
        elif opcion == 11:
            decision = False
            print("Saliendo...")

def generarTablaPDF():
    clearConsole()
    dao = DAO()
    envasados = dao.listar("Envasado")
    funciones.generarTablaPDF(envasados)

sub_menu()