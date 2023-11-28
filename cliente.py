import socket

# se declaran variables de conexión
host = '127.0.0.1'
port = 3103

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:       
    cliente.connect((host, port))
    while True:
        print("Conexión Exitosa")

        # el servidor pide una ruta
        msg_servidor = cliente.recv(1024)
  
        # respuesta
        respuesta = input(msg_servidor.decode('utf-8'))
        cliente.sendall(respuesta.encode('utf-8'))

        
        #mensaje 2
        msg_servidor2 = cliente.recv(1024)
        if not msg_servidor2:
            break
        
        #respuesta 2
        respuesta2 = input(msg_servidor2.decode('utf-8'))
        cliente.sendall(respuesta2.encode('utf-8'))
        
        #mensaje 3
        msg_servidor3 = cliente.recv(1024)
        if not msg_servidor3:
            break
        
        #respuesta 3
        respuesta3 = input(msg_servidor3.decode('utf-8'))
        cliente.sendall(respuesta3.encode('utf-8'))
        
        #mensaje 4
        msg_servidor4 = cliente.recv(1024)
        
        #respuesta 4
        respuesta4 = input(msg_servidor4.decode('utf-8'))
        cliente.sendall(respuesta4.encode('utf-8'))
        
        msg_servidor5 = cliente.recv(1024)
        if not msg_servidor5:
            break
        print(msg_servidor5.decode('uft-8'))


    print("Cerrando cliente")
    cliente.close()

    
    