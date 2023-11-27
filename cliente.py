import socket as sk

#Declaramos variables de conexion
host = '127.0.0.1'
port = 3103

with sk.socket(sk.AF_INET, sk.SOCK_STREAM) as cliente:
    cliente.connect((host,port))
    
    print("Conexión exitosa")
    
    msj = "Hola, ¿En qué puedo ayudarle?"
    cliente.sendall(msj.encode('utf-8'))
    
    
    #Aquí le pones lo que lleve del socket
    data = cliente.recv(1024)
    print(f"Dice {data.decode('uft-8')}")
    
    print("Cerrando cliente")