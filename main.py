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
         
    match opcion:
        case 1: funciones.listarRecepciones(recepciones),
        case 2: dao.registrarRecepcion(funciones.pedirDatosRegistroRecepcion()),
        case 3: dao.actualizarRecepcion(funciones.pedirDatosActualizacionRecepcion(recepciones)),
        case 4: dao.eliminarRecepcion(funciones.pedirDatosEliminarRecepcion(recepciones)),
        case _: print("Opción no válida...")

        
def opcionesProducto(opcion: int,entidadAUsar: string):
    clearConsole()
    dao = DAO()
    productos = dao.listar(entidadAUsar)
         
    match opcion:
        case 1: funciones.listarProductos(productos),
        case 2: dao.registrarProducto(funciones.pedirDatosRegistroProducto()),
        case 3: dao.actualizarProducto(funciones.pedirDatosActualizacionProducto(productos)),
        case 4: dao.eliminarProducto(funciones.pedirDatosEliminarProducto(productos)),
        case _: print("Opción no válida...")

def opcionesEnvasado(opcion: int,entidadAUsar: string):
    clearConsole()
    dao = DAO()
    envasados = dao.listar(entidadAUsar)
         
    match opcion:
        case 1: funciones.listarEnvasados(envasados),
        case 2: dao.registrarEnvasado(funciones.pedirDatosRegistroEnvasado()),
        case 3: dao.actualizarEnvasado(funciones.pedirDatosActualizacionEnvasado(envasados)),
        case 4: dao.eliminarEnvasado(funciones.pedirDatosEliminarEnvasado(envasados)),
        case _: print("Opción no válida...")

def opcionesMuestreo(opcion: int,entidadAUsar: string):
    clearConsole()
    dao = DAO()
    muestreos = dao.listar(entidadAUsar)
         
    match opcion:
        case 1: funciones.listarMuestreos(muestreos),
        case 2: dao.registrarMuestreo(funciones.pedirDatosRegistroMuestreo()),
        case 3: dao.actualizarMuestreo(funciones.pedirDatosActualizacionMuestreo(muestreos)),
        case 4: dao.eliminarMuestreo(funciones.pedirDatosEliminarMuestreo(muestreos)),
        case _: print("Opción no válida...")

def ejecutarOpcion(opcion: int,entidadAUsar: string):
    clearConsole()
    DAO()

    match entidadAUsar :
        case "Recepcion": opcionesRecpcion(opcion,entidadAUsar)
        case "Envasado": opcionesEnvasado(opcion,entidadAUsar)
        case "Muestreo": opcionesMuestreo(opcion,entidadAUsar)
        case "Producto": opcionesProducto(opcion,entidadAUsar)
        case _: print("Entidad no válida...")

login()