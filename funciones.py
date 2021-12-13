# Metodo para listar las recepciones
def listarRecepciones(listaEntidades):
    print("\Recepcion: \n")
    contador = 1
    for entidad in listaEntidades:
        datos = "{0}. codigo: {1} | fecha: {2} | totalUnidades: {3} |  Apicultor_Persona_cedula: {4} | " \
                "Apicultor_Persona_email: {5} | Conductor_Persona_cedula: {6} | Conductor_Persona_email: {7} | " \
                "Lote_codigo: {8} "
        print(datos.format(contador, entidad[0], entidad[1], entidad[2], entidad[3], entidad[4], entidad[5], entidad[6], entidad[7]))

# Metodo para pedir los datos de la recepcion
def pedirDatosRegistroRecepcion():
    codigo = int(input("Ingrese el código de la recepcion: "))
    fecha = input("Ingrese la fecha de la recepción: ")
    totalUnidades = int(input("Ingrese el total de unidades: "))
    cedulaApicultor = int(input("Ingrese la cédula del apicultor: "))
    emailApicultor = input("Ingrese el email del apicultor: ")
    cedulaConductor = int(input("Ingrese la cédula del conductor: "))
    emailConductor = input("Ingrese el email del conductor: ")
    codigoLote = int(input("Ingrese el código del lote: "))

    recepcion = (codigo, fecha, totalUnidades, cedulaApicultor, emailApicultor, cedulaConductor, emailConductor, codigoLote)
    return recepcion

# Metodo para solicitar los datos de actualización de recepcion
def pedirDatosActualizacionRecepcion(recepciones):
    codigo = int(input("Ingrese el código de la recepcion: "))
    existeCodigo = False
    for cur in recepciones:
        if cur[0] == codigo:
            existeCodigo = True
            break

    if existeCodigo:
        fecha = input("Ingrese la nueva fecha de la recepción: ")
        totalUnidades = int(input("Ingrese el nuevo total de unidades: "))
        cedulaApicultor = int(input("Ingrese la nueva cédula del apicultor: "))
        emailApicultor = input("Ingrese el nuevo email del apicultor: ")
        cedulaConductor = int(input("Ingrese la nueva cédula del conductor: "))
        emailConductor = input("Ingrese el nuevo email del conductor: ")
        codigoLote = int(input("Ingrese el nuevo código del lote: "))

        recepcion = (codigo, fecha, totalUnidades, cedulaApicultor, emailApicultor, cedulaConductor, emailConductor, codigoLote)
        return recepcion
    else:
        print("El código ingresado no existe")
        return None


# Metodo para solicitar los datos para eliminar una recepcion
def pedirDatosEliminarRecepcion(recepciones):

    existeCodigo = False
    codigoEliminar = int(input("Ingrese el código del producto a eliminar: "))
    for cur in recepciones:
        if cur[0] == codigoEliminar:
            existeCodigo = True
            break

    if existeCodigo:
        return codigoEliminar
    else:
        print("El código ingresado no existe")
        return None


# Metodo para listar los productos
def listarProductos(listaEntidades):
    print("\Producto: \n")
    contador = 1
    for entidad in listaEntidades:
        datos = "{0}. idProducto: {1} | fecha: {2} | peso_neto: {3} |  peso_bruto: {4} | Recepcion_codigo: {5} | " \
                "Recepcion_fecha: {6} | Tipo_Producto_idTipo: {7} "
        print(datos.format(contador, entidad[0], entidad[1], entidad[2], entidad[3], entidad[4], entidad[5], entidad[6]))

# Metodo para solicitar los datos para registrar un producto
def pedirDatosRegistroProducto():
    idProducto = int(input("Ingrese el codigo del producto: "))
    fecha = input("Ingrese la fecha del producto: ")
    peso_neto = input("Ingrese el peso neto del producto: ")
    peso_bruto = input("Ingrese el peso bruto del producto: ")
    Recepcion_codigo = int(input("Ingrese el codigo de la recepcion: "))
    Recepcion_fecha = input("Ingrese la fecha de la recepcion: ")
    Tipo_Producto_idTipo = int(input("Ingrese el codigo del tipo de producto: "))

    producto = (idProducto, fecha, peso_neto, peso_bruto, Recepcion_codigo, Recepcion_fecha, Tipo_Producto_idTipo)
    return producto

# Metodo para solicitar los datos para actualizar un producto
def pedirDatosActualizacionProducto(productos):
    existeCodigo = False
    idProducto = int(input("Ingrese el código del producto a editar: "))
    for cur in productos:
        if cur[0] == idProducto:
            existeCodigo = True
            break

    if existeCodigo:
        fecha = input("Ingrese la nueva fecha del producto: ")
        peso_neto = input("Ingrese el nuevo peso neto del producto: ")
        peso_bruto = input("Ingrese el nuevo peso bruto del producto: ")
        Recepcion_codigo = int(input("Ingrese el nuevo codigo de la recepcion: "))
        Recepcion_fecha = input("Ingrese la nueva fecha de la recepcion: ")
        Tipo_Producto_idTipo = int(input("Ingrese el nuevo codigo del tipo de producto: "))

        producto = (idProducto, fecha, peso_neto, peso_bruto, Recepcion_codigo, Recepcion_fecha, Tipo_Producto_idTipo)
    return producto

# Metodo para solicitar los datos para eliminar un producto
def pedirDatosEliminarProducto(productos):
    existeCodigo = False
    codigoEliminar = int(input("Ingrese el código del producto a eliminar: "))
    for cur in productos:
        if cur[0] == codigoEliminar:
            existeCodigo = True
            break

    if not existeCodigo:
        codigoEliminar = ""

    return codigoEliminar

# Metodo para listar los datos de envasado
def listarEnvasados(listaEntidades):
    print("\ + {EntidadAUsar} + s: \n")
    contador = 1
    for entidad in listaEntidades:
        datos = "{0}. Código: {1} | Fecha: {2}  lote_codigo {3}  Muestreo {4}"
        print(datos.format(contador, entidad[0], entidad[1], entidad[2],entidad[3]))
        contador = contador + 1
    print(" ")

# Metodo para solicitar los datos para registrar un envasado
def pedirDatosRegistroEnvasado():
    codigo = int(input("Ingrese el código del envasado: "))
    fecha = input("Ingrese la fecha del envasado: ")
    codigoLote= int(input("Ingrese codigo lote: "))
    codigoLoteMuestreo = int(input("Ingrese el codigo del muestreo: "))

    envasado = (codigo,fecha, codigoLote,codigoLoteMuestreo)

    return envasado

# Metodo para solicitar los datos para actualizar un envasado
def pedirDatosActualizacionEnvasado(envasados):
    codigoEditar = int(input("Ingrese el código del envasado a editar: "))
    existeCodigo = False
    for cur in envasados:
        if cur[0] == codigoEditar:
            existeCodigo = True
            break

    if existeCodigo:
        fechaEnvase = input("Ingrese la fecha a modificar: ")
        loteCodigo = input("Ingrese lote codigo a modificar: ")
        codigoMuestreo = input ("Ingrese el codigo del muestreo para modificar: ")

        envasado = (codigoEditar, fechaEnvase,loteCodigo, codigoMuestreo)
    return envasado

# Metodo para solicitar los datos para eliminar un envasado
def pedirDatosEliminarEnvasado(envasados):
    existeCodigo = False
    codigoEliminar = int(input("Ingrese el código del curso a eliminar: "))
    for envase in envasados:
        if envase[0] == codigoEliminar:
            existeCodigo = True
            break

    if not existeCodigo:
        codigoEliminar = ""

    return codigoEliminar

# Metodo para listar los datos del muestreo
def listarMuestreos(listaEntidades):
    print("\ + {Muestreo} + s: \n")
    contador = 1
    for entidad in listaEntidades:
        datos = "{0}. Código: {1} | Fecha: {2}  Unidades aceptadas: {3} | Cédula empleado: {4} | Email empleado: {5}"
        print(datos.format(contador, entidad[0], entidad[1], entidad[2],entidad[3], entidad[4]))
        contador = contador + 1
    print(" ")

# Metodo para solicitar los datos para registrar un muestreo
def pedirDatosRegistroMuestreo():
    codigo = int(input("Ingrese el código del muestreo: "))
    fecha = input("Ingrese la fecha del muestreo: ")
    unidades_aceptadas = int(input("Ingrese las unidades aceptadas: "))
    Empleado_Persona_cedula = int(input("Ingrese la cedula del empleado: "))
    Empleado_Persona_email = input("Ingrese el email del empleado: ")

    muestreo = (codigo,fecha,unidades_aceptadas,Empleado_Persona_cedula,Empleado_Persona_email)

    return muestreo

# Metodo para solicitar los datos para actualizar un muestreo
def pedirDatosActualizacionMuestreo(muestreos):
    codigoEditar = int(input("Ingrese el código del muestreo a editar: "))
    existeCodigo = False
    for cur in muestreos:
        if cur[0] == codigoEditar:
            existeCodigo = True
            break

    if existeCodigo:
        fechaMuestreo = input("Ingrese la fecha a modificar: ")
        unidadesAceptadas = input("Ingrese las unidades aceptadas a modificar: ")
        cedulaEmpleado = input("Ingrese la cedula del empleado a modificar: ")
        emailEmpleado = input("Ingrese el email del empleado a modificar: ")

        muestreo = (codigoEditar, fechaMuestreo,unidadesAceptadas,cedulaEmpleado,emailEmpleado)
    return muestreo

# Metodo para solicitar los datos para eliminar un muestreo
def pedirDatosEliminarMuestreo(muestreos):
    existeCodigo = False
    codigoEliminar = int(input("Ingrese el código del muestreo a eliminar: "))
    for cur in muestreos:
        if cur[0] == codigoEliminar:
            existeCodigo = True
            break

    if not existeCodigo:
        codigoEliminar = ""

    return codigoEliminar

# Metodo para solicitar los datos de login
def pedirDatosLogin():
    correo = input("Ingrese el correo: ")
    password = int(input("Ingrese la contraseña: "))

    login = (correo,password)

    return login
