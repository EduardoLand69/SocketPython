import socket as sk
import time as tm

#Declaramos variables de conexion
host = '127.0.0.1'
port = 3103

with sk.socket(sk.AF_INET, sk.SOCK_STREAM) as cliente:
    cliente.connect((host,port))
    
    print("Conexión exitosa")
    
    msg_servidor = cliente.recv(1024) #Ingresa un directorio para empezar a trabajar
    #capturar una respuesta
    respuesta_cliente = input(msg_servidor.decode('utf-8'))
    #enviar el mensaje al servidor
    cliente.sendall(respuesta_cliente.encode('utf-8'))
    
    #bloque si existe el directorio
    msg_servidor = cliente.recv(1024) #el servidor esta diciendo ok o no
    
    if msg_servidor.decode('utf-8') == "ok": #el servidor tiene el directorio
        #pasar a pedir el archvio
        perdirArchivo = cliente.recv(1024) #Ingresa el nombre del archivo con el que quieres trabajar
        respuesta_cliente = input(perdirArchivo.decode('utf-8'))
        cliente.sendall(respuesta_cliente.encode('utf-8')) #se envio el archivo al servidor
        
        #casos para saber si existe el archivo o no
        msg_servidor = cliente.recv(1024) #el servidor esta diciendo ok o no
        
        if msg_servidor.decode('utf-8') == "ok":
            #el servidor pregunta si se quiere escribir en el archivo
            escribirContenido = cliente.recv(1024)
            respuesta_cliente = input(escribirContenido.decode('utf-8'))
            if respuesta_cliente == "y" or respuesta_cliente == "Y":
                #pedir al  cliente el contenido
                contenido = input("Escribir el contenido: ")
                cliente.sendall(contenido.encode('utf-8'))
                print("Se mando el contenido al archivo :)")
                tm.sleep(3)
                exit
            if respuesta_cliente == "n" or respuesta_cliente == "N":
                print("No se escribio nada en el archivo")
                tm.sleep(3)
                exit
            pass
        
        #el archivo no existe el servidor
        if msg_servidor.decode('utf-8') == "no":
            ##recibir respuesta del servidor
            pregunta= cliente.recv(1024) #"Quieres crear el archivo?
            respuesta_cliente = input(pregunta.decode('utf-8'))
            if respuesta_cliente == "y" or respuesta_cliente == "Y":
                cliente.sendall(respuesta_cliente.encode('utf-8'))
                #le decimos al servidor que si queremos crear el archivo
                #bloque para controlar si se quiere crear el archivo
            if respuesta_cliente == "n" or respuesta_cliente == "N":
                print("No se creo el archivo :(")
                tm.sleep(3)
                exit

    if msg_servidor.decode('utf-8') == "no": #el servidor no tiene el directorio
        
        pass
    
    print("Cerrando cliente")