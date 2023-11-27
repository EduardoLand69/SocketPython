import socket as sk #importamos el socker y trabajaremos con el como sk

HOST = '127.0.0.1'
PORT = 3103

with sk.socket(sk.AF_INET, sk.SOCK_STREAM) as s:
    s.bind((HOST,PORT)) #unir la direccion ip con el puerto
    s.listen() #aceptar a 10 clientes
    
    print("Esperando conexion...")
    
    conexion,ip_cliente = s.accept() #aceptar las conexiones entrantes
    
    with conexion:
        print(f"Se establecio la conexion con: {ip_cliente}")
        #recibir mensaje cliene
        cliente_msg = conexion.recv(1024)
        print(f"Cliente: {cliente_msg}")
        
    print("Desconectando y apagando servidor...")