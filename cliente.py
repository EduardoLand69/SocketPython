import socket as sk
import time as tm

#Declaramos variables de conexion
host = '127.0.0.1'
port = 3103

with sk.socket(sk.AF_INET, sk.SOCK_STREAM) as cliente:
    cliente.connect((host,port))
    
    print("Conexión exitosa")
    
    ####Enviar una respuesta al servidor
    #El servidor esta pidiendo una ruta
    msg_servidor = cliente.recv(1024)
    #capturar una respuesta
    respuesta_cliente = input(msg_servidor.decode('utf-8'))
    #enviar el mensaje al servidor
    cliente.sendall(respuesta_cliente.encode('utf-8'))
    
    ####Enviar una respuesta al servidor
    #El servidor esta preguntando si se quiere crear el direcotorio o no
    msg_servidor = cliente.recv(1024)
    #capturar una respuesta
    respuesta_cliente = input(msg_servidor.decode('utf-8'))
    #enviar el mensaje al servidor
    cliente.sendall(respuesta_cliente.encode('utf-8'))
    if respuesta_cliente == "y": #¿Quieres crear el directorio?
        #El servidor esta pidiendo una ruta
        msg_servidor = cliente.recv(1024)
        #capturar una respuesta
        respuesta_cliente = input(msg_servidor.decode('utf-8'))
        #enviar el mensaje al servidor
        cliente.sendall(respuesta_cliente.encode('utf-8'))
        if respuesta_cliente == "y":#¿Quieres crear el archivo?
            msg_servidor = cliente.recv(1024)
            respuesta_cliente = input(msg_servidor.decode('utf-8'))
            cliente.sendall(respuesta_cliente.encode('utf-8'))
        elif respuesta_cliente == "n":
            print("El cliente se cerrará")
            tm.sleep(3)
            exit
    elif respuesta_cliente == "n":
        print("El cliente se cerrará")
        tm.sleep(3)
        exit
    
    ####Enviar una respuesta al servidor
    #El servidor esta pidiendo una archivo
    msg_servidor = cliente.recv(1024)
    #capturar una respuesta
    respuesta_cliente = input(msg_servidor.decode('utf-8'))
    #enviar el mensaje al servidor
    cliente.sendall(respuesta_cliente.encode('utf-8'))

    ####Enviar una respuesta al servidor
    #El servidor esta preguntando si se quiere crear el archivo
    msg_servidor = cliente.recv(1024)
    #capturar una respuesta
    respuesta_cliente = input(msg_servidor.decode('utf-8'))
    #enviar el mensaje al servidor
    cliente.sendall(respuesta_cliente.encode('utf-8'))
    
    
    print("Cerrando cliente")