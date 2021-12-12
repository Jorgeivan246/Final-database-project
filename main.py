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
    while(continuar):
        opcion_correcta = False
        while(not opcion_correcta):
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


def ejecutarOpcion(opcion: int,entidadAUsar: string):
    dao = DAO()

    if opcion == 1:
        try:
            listaEntidades = dao.listar("producto")
            if len(listaEntidades) > 0:
                funciones.listarProductos(listaEntidades,entidadAUsar)
            else:
                print("No se encontraron productos...")
        except:
            print("Ocurrió un error...")
    elif opcion == 2:
        producto = funciones.pedirDatosRegistroProducto()
        try:
            dao.registrarTipoLicencia(producto)
        except:
            print("Ocurrió un error...")
    elif opcion == 3:
        try:
            listaEntidades = dao.listar()
            if len(listaEntidades) > 0:
                entidad = funciones.pedirDatosActualizacion(listaEntidades)
                if entidad:
                    dao.actualizar(entidad,entidadAUsar)
                else:
                    print("Código de curso a actualizar no encontrado...\n")
            else:
                print("No se encontraron cursos...")
        except:
            print("Ocurrió un error...")
    elif opcion == 4:
        try:
            listaEntidades = dao.listar("producto")
            if len(listaEntidades) > 0:
                codigoEliminar = funciones.pedirDatosEliminacionProducto(listaEntidades)
                if not(codigoEliminar == ""):
                    dao.eliminarProducto(codigoEliminar)
                else:
                    print("Código de producto no encontrado...\n")
            else:
                print("No se encontraron productos...")
        except:
            print("Ocurrió un error...")
    else:
        print("Opción no válida...")


sub_menu();
