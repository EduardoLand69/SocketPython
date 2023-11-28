import socket

#Declaramos variables de conexion
host = '127.0.0.1'
port = 3103

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
    cliente.connect((host,port))
    
    print("Conexión exitosa")
    
    ####Enviar una respuesta al servidor
    #El servidor esta pidiendo una ruta
    msg_servidor = cliente.recv(1024)
    #capturar una respuesta
    respuesta_cliente = input(msg_servidor.decode('utf-8'))
    #enviar el mensaje al servidor
    cliente.sendall(respuesta_cliente.encode('utf-8'))
    
    ####Enviar una respuesta al servidor de si o no
    #El servidor esta pidiendo una ruta
    msg_servidor = cliente.recv(1024)
    #capturar una respuesta
    respuesta_cliente = input(msg_servidor.decode('utf-8'))
    #enviar el mensaje al servidor
    cliente.sendall(respuesta_cliente.encode('utf-8'))
    
    
    ####Enviar una respuesta al servidor para buscar el archivo
    #El servidor esta pidiendo una ruta
    msg_servidor = cliente.recv(1024)
    #capturar una respuesta
    respuesta_cliente = input(msg_servidor.decode('utf-8'))
    #enviar el mensaje al servidor
    cliente.sendall(respuesta_cliente.encode('utf-8'))
    
    print("Cerrando cliente")