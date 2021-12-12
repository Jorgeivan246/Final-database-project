from DAO import DAO
import funciones
import string

def sub_menu():
    
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
    dao = DAO()
    recepciones = dao.listar(entidadAUsar)
         
    match opcion:
        case 1: funciones.listarRecepciones(recepciones),
        case 2: dao.registrarRecepcion(funciones.pedirDatosRegistroRecepcion()),
        case 3: dao.actualizarRecepcion(funciones.pedirDatosActualizacionRecepcion(recepciones)),
        case 4: dao.eliminarRecepcion(funciones.pedirDatosEliminarRecepcion(recepciones)),
        case _: print("Opción no válida...")

        
def opcionesProducto(opcion: int,entidadAUsar: string):
    dao = DAO()
    productos = dao.listar(entidadAUsar)
         
    match opcion:
        case 1: funciones.listarProductos(productos),
        case 2: dao.registrarProducto(funciones.pedirDatosRegistroProducto()),
        case 3: dao.actualizarProducto(funciones.pedirDatosActualizacionProducto(productos)),
        case 4: dao.eliminarProducto(funciones.pedirDatosEliminarProducto(productos)),
        case _: print("Opción no válida...")

def opcionesEnvasado(opcion: int,entidadAUsar: string):
    dao = DAO()
    envasados = dao.listar(entidadAUsar)
         
    match opcion:
        case 1: funciones.listarEnvasados(envasados),
        case 2: dao.registrarEnvasado(funciones.pedirDatosRegistroEnvasado()),
        case 3: dao.actualizarEnvasado(funciones.pedirDatosActualizacionEnvasado(envasados)),
        case 4: dao.eliminarEnvasado(funciones.pedirDatosEliminarEnvasado(envasados)),
        case _: print("Opción no válida...")

def ejecutarOpcion(opcion: int,entidadAUsar: string):
    DAO()

    match entidadAUsar :
        case "Recepcion": opcionesRecpcion(opcion,entidadAUsar)
        case "Envasado": opcionesEnvasado(opcion,entidadAUsar)
        case "Muestreo": funciones.opcionesMuestreo(opcion,entidadAUsar)
        case "Producto": opcionesProducto(opcion,entidadAUsar)
        case _: print("Entidad no válida...")


sub_menu()
