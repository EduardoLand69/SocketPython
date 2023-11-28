import socket as sk #importamos el socker y trabajaremos con el como sk
import os #esta lib la usaremos para trabajar con los archivos
import implementacion_try as lmcs

# Configuración del servidor
HOST = '127.0.0.1'
PORT = 3103

pedirRuta = "Ingresa un directorio para empezar a trabar: "
pedirArchivo = "Ingresa el nombre del archivo con el que quieres trabajar: "



with sk.socket(sk.AF_INET, sk.SOCK_STREAM) as s:
    s.bind((HOST,PORT)) #unir la direccion ip con el puerto
    s.listen() #aceptar a 10 clientes
    
    print("Esperando conexion...")
    
    cliente,ip_cliente = s.accept() #aceptar las conexiones entrantes
    
    with cliente:
        print(f"Se establecio la conexion con: {ip_cliente}")
        #pedir al cliente que envio un archivo en cuanto la conexion se realiza: 
        cliente.sendall(pedirRuta.encode('utf-8'))
        #recibir el mensaje la conexion:
        recibirRuta = cliente.recv(1024)
        #verificar que la ruta que llego en verdad sea una ruta
        try:
            lmcs.esDirectorio(recibirRuta.decode('utf-8'))
            #ahora que sabemos que cumple con la estructura de un directorio
            if lmcs.buscarDirectorio(recibirRuta.decode('utf-8')):
                #print("Directorio encontrado")
                pass
            else:
                #print("Directorio no encontrado")
                #lo que pasa si el directorio no existe
                
                #preguntar si se quiere crear el directorio
                preguntarCrearDir = "Quieres crear el directorio? [y/n]"
                cliente.sendall(preguntarCrearDir.encode('utf-8'))
                
                #recibir la respuesta del cliente
                recibirRespuesta = cliente.recv(1024)
                #mandar la respuesta del cliente a la funcion de crearDirectorio
                try:
                    if lmcs.crearDirectorio(recibirRuta.decode('utf-8'), recibirRespuesta.decode('utf-8')):
                        #se direcotrio, proceder con el demas codigo
                        
                        #pedir el archivo a buscar
                        cliente.sendall(pedirArchivo.encode('utf-8'))
                        #recibir el archivo
                        recibirArchivo = cliente.recv(1024)
                        #buscar el archivo
                        if lmcs.buscarArchivo(recibirRuta.decode('utf-8'), recibirArchivo.decode('utf-8')):
                            #archivo encontrado
                            print("El archivo se encuentra en el directorio")
                            
                            #bloque de codigo para saber que hacer con el archivo
                            
                            pass
                        else:
                            #archivo no encontrado
                            print("El archivo no se encuentra en el directorio")
                            
                            #preguntar si se quiere crear el archivo
                            preguntarCrearArchivo = "Quieres crear el archivo? [y/n]"
                            cliente.sendall(preguntarCrearArchivo.encode('utf-8'))
                            
                            #recibir la respuesta del cliente
                            recibirRespuesta = cliente.recv(1024)
                            #mandar la respuesta del cliente a la funcion de crearArchivo
                            try:
                                if lmcs.crearArchivo(recibirRuta.decode('utf-8'), recibirArchivo.decode('utf-8'), recibirRespuesta.decode('utf-8')):
                                    #se creo el archivo, proceder con el demas codigo
                                    pass
                                else:
                                    #no se creo el archivo (se cierra la conexion)
                                    pass
                            except Exception as e:
                                print(e)
                    else:
                        #no se crea el directorio (falta saber que pasa despues, porque si llegamos aqui la conexion se cierra)
                        pass
                except Exception as e:
                    print(e)
                    
                pass
        except Exception as e:
            print(e)
        
    print("Desconectando y apagando servidor...")