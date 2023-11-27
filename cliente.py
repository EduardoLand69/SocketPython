import socket

#Declaramos variables de conexion
host = '127.0.0.1'
port = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
    cliente.connect((host,port))
    
    print("Conexión exitosa")
    
    msj = "Hola, ¿En qué puedo ayudarle?"
    cliente.sendall(msj.encode('utf-8'))
    
    
    #Aquí le pones lo que lleve del socket
    data = socket.recv(1024)
    print(f"Dice {data.decode('uft-8')}")
    
    print("Cerrando cliente")