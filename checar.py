import socket as sk

#Declaramos variables de conexion
host = '127.0.0.1'
port = 3103

with sk.socket(sk.AF_INET, sk.SOCK_STREAM) as cliente:
    cliente.connect((host,port))
    
    print("Petición de archivo")
    respuesta = cliente.recv(1024)
    
    preguntarArch = input(respuesta.decode('utf-8'))
    
    cliente.sendall(preguntarArch.encode('utf-8'))
    
    