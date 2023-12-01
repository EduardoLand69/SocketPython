import os

#verificar que el string no este vacio
def esVacio(ruta):
    if ruta!= "":
        #no esta vacio
        return True
    else:
        #esta vacio
        raise Exception ("La cadena que se envio esta vacia")
        return False
#comprobar que el directorio exista en la maquina
def buscarDirectorio(ruta):
    if os.path.exists(ruta):
        #ya existe
        return True
    else:
        #no existe
        return False
    
#preguntar si se quiere crear un directorio
def crearDirectorio(ruta, respuesta):
    if respuesta == "y":
        #si se quiere crear el directorio
        os.mkdir(ruta)
        return True
    elif respuesta == "n":
        #si no se quiere crear el directorio
        return False
    else:
        #respuesta no valida
        raise Exception (f"{respuesta} no es una respuesta valida!")

#funcion para verificar que el mensaje es un archivo
def esArchivo(ruta, archivo):
    pass

#buscar el archivo en el directorio
def buscarArchivo(ruta, archivo):
    if os.path.exists(ruta + "/" + archivo):
        #ya existe
        return True
    else:
        #no existe
        return False
    
    #funcion para crear el archivo
def crearArchivo(ruta,archivo,respuesta):
    if respuesta == "y":
        #si se quiere crear el archivo
        archivo = open(f"{ruta}{archivo}", "w")
        archivo.close()
        return True
    elif respuesta == "n":
        #si no se quiere crear el archivo
        return False
    else:
        #respuesta no valida
        raise Exception (f"{respuesta} no es una respuesta valida!")
    
#crear una funcion que verifique si el archivo esta vacio o no
def archivoVacio(ruta,archivo):
    #esta funcion nos sirve para comprobar si un archivo tiene contenido escrito o no - Si el archivo tiene contenido, entonces preguntamos sobre escribir, sino, solo pedimos contenido
    with open(f"{ruta}/{archivo}", 'r') as file:
        contenido = file.read()
        if contenido:
            return False
        else:
            return True
        
#funcion para escribir en el archivo
def escribir(ruta,archivo,contenido):
    with open(f"{ruta}{archivo}", "w") as arch:
        arch.write(contenido)
    #print(f"Archivo, {archivo}, escrito correctamente")