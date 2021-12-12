def listarProductos(listaEntidades,entidadAUsar):
    print("\Producto: \n")
    contador = 1
    for entidad in listaEntidades:
        datos = "{0}. idProducto: {1} | fecha: {2} | peso_neto: {3} |  peso_bruto: {4} | Recepcion_codigo: {5} | " \
                "Recepcion_fecha: {6} | Tipo_Producto_idTipo: {7} "
        print(datos.format(contador, entidad[0], entidad[1], entidad[2], entidad[3], entidad[4], entidad[5], entidad[6]))


def pedirDatosRegistroProducto():
    idProducto = int(input("Ingrese código: "))
    fecha = input("Ingrese fecha: ")
    peso_neto = input("Ingrese el peso neto: ")
    peso_bruto = input("Ingrese el peso bruto: ")
    Recepcion_codigo = int(input("Ingrese el código de la recepcion: "))
    Recepcion_fecha = input("Ingrese la fecha de la recepción: ")
    Tipo_Producto_idTipo = int(input("Ingrese código del tipo de producto: "))

    producto = (idProducto, fecha, peso_neto, peso_bruto, Recepcion_codigo, Recepcion_fecha, Tipo_Producto_idTipo)
    return producto

def pedirDatosEliminacionProducto(productos):
    listarProductos(productos)
    existeCodigo = False
    codigoEliminar = input("Ingrese el código del producto a eliminar: ")
    for cur in productos:
        if cur[0] == codigoEliminar:
            existeCodigo = True
            break

    if not existeCodigo:
        codigoEliminar = ""

    return codigoEliminar

def pedirDatosRegistro():
    codigoCorrecto = False
    while(not codigoCorrecto):
        codigo = input("Ingrese código: ")
        if len(codigo) == 6:
            codigoCorrecto = True
        else:
            print("Código incorrecto: Debe tener 6 dígitos.")

    nombre = input("Ingrese nombre: ")

    creditosCorrecto = False
    while(not creditosCorrecto):
        creditos = input("Ingrese créditos: ")
        if creditos.isnumeric():
            if (int(creditos) > 0):
                creditosCorrecto = True
                creditos = int(creditos)
            else:
                print("Los créditos deben ser mayor a 0.")
        else:
            print("Créditos incorrectos: Debe ser un número únicamente.")

    curso = (codigo, nombre, creditos)
    return curso

def pedirDatosActualizacion(cursos):
    listarProductos(cursos)
    existeCodigo = False
    codigoEditar = input("Ingrese el código del curso a editar: ")
    for cur in cursos:
        if cur[0] == codigoEditar:
            existeCodigo = True
            break

    if existeCodigo:
        nombre = input("Ingrese nombre a modificar: ")

        creditosCorrecto = False
        while(not creditosCorrecto):
            creditos = input("Ingrese créditos a modificar: ")
            if creditos.isnumeric():
                if (int(creditos) > 0):
                    creditosCorrecto = True
                    creditos = int(creditos)
                else:
                    print("Los créditos deben ser mayor a 0.")
            else:
                print("Créditos incorrectos: Debe ser un número únicamente.")

        curso = (codigoEditar, nombre, creditos)
    else:
        curso = None

    return curso
