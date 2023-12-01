import socket as sk #importamos el socker y trabajaremos con el como sk
import os #esta lib la usaremos para trabajar con los archivos
import implementacion_try as lmcs
import time as tm

# Configuración del servidor
HOST = '127.0.0.1'
PORT = 3103

pedirRuta = "Ingresa un directorio para empezar a trabajar: "
pedirArchivo = "Ingresa el nombre del archivo con el que quieres trabajar: "

with sk.socket(sk.AF_INET, sk.SOCK_STREAM) as s:
    s.bind((HOST,PORT)) #unir la direccion ip con el puerto
    s.listen(2) #aceptar a 10 clientes
    
    print("Esperando conexion...")
    
    cliente,ip_cliente = s.accept() #aceptar las conexiones entrantes
    
    with cliente:
        print(f"Se establecio la conexion con: {ip_cliente}")
        #pedir al cliente que envio un archivo en cuanto la conexion se realiza: 
        cliente.sendall(pedirRuta.encode('utf-8'))
        #recibir el mensaje la conexion:
        recibirRuta = cliente.recv(1024)
        #verificar que la ruta que llego en verdad sea una ruta
        print(f"ruta que envio el cliente: {recibirRuta.decode('utf-8')}")
        try:
            lmcs.esVacio(recibirRuta.decode('utf-8'))
            #ahora que sabemos que cumple con la estructura de un directorio
            if lmcs.buscarDirectorio(recibirRuta.decode('utf-8')): ###########################
                ####################################
                
                ok = "ok"
                cliente.sendall(ok.encode('utf-8'))
                
                ####################################
                
                #acciones a realizar si el directorio existe
                #si el directorio existe, pasar a pedir el archivo
                cliente.sendall(pedirArchivo.encode('utf-8'))
                #recibir el archivo
                recibirArchivo = cliente.recv(1024)
                #buscar el archivo
                if lmcs.buscarArchivo(recibirRuta.decode('utf-8'), recibirArchivo.decode('utf-8')):
                    #archivo encontrado
                    cliente.sendall("ok".encode('utf-8'))#### se manda la verificación al servidor
                    print(f"El archivo se encuentra en el directorio {recibirRuta.decode('utf-8')}")
                    
                    #bloque de codigo para saber que hacer con el archivo ######
                    #saber si el archivo esta vaacio
                    if lmcs.archivoVacio(recibirRuta.decode('utf-8'),recibirArchivo.decode('utf-8')):
                        print("El archivo esta vacio")
                        #preguntar si se quiere meter contenido al archivo
                        preguntarContenidoArchivo = "Quieres insertar contenido a tu archivo? [y/n]: "
                        cliente.sendall(preguntarContenidoArchivo.encode('utf-8'))
                        
                        #recibir la respuesta del cliente
                        contenidoParaArchvo = cliente.recv(1024)
                        #escribirmos en el archivo
                        lmcs.escribir(recibirRuta.decode('utf-8'),recibirArchivo.decode('utf-8'),contenidoParaArchvo.decode('utf-8'))
                    else:
                        print("El archivo no esta vacio")
                        #preguntar si se quiere sobre escrbiir el archivo
                        preguntarContenidoArchivo = "Quieres sobreescribir tu archivo? [y/n]: "
                        cliente.sendall(preguntarContenidoArchivo.encode('utf-8'))
                        
                        #recibir la respuesta del cliente
                        contenidoParaArchvo = cliente.recv(1024)
                        #escribirmos en el archivo
                        lmcs.escribir(recibirRuta.decode('utf-8'),recibirArchivo.decode('utf-8'),contenidoParaArchvo.decode('utf-8'))
                    pass
                else:
                    #archivo no encontrado
                    cliente.sendall("no".encode('utf-8'))#### se manda la verificación al servidor
                    print(f"El archivo no se encuentra en el directorio {recibirRuta.decode('utf-8')}")
                    #preguntar si se quiere crear el archivo
                    preguntarCrearArchivo = "Quieres crear el archivo? [y/n]: "
                    cliente.sendall(preguntarCrearArchivo.encode('utf-8'))
                    
                    #recibir la respuesta del cliente
                    recibirRespuesta = cliente.recv(1024)
                    #mandar la respuesta del cliente a la funcion de crearArchivo
                    try:
                        if lmcs.crearArchivo(recibirRuta.decode('utf-8'), recibirArchivo.decode('utf-8'), recibirRespuesta.decode('utf-8')):
                            #se creo el archivo, proceder con el demas codigo
                            print(f"El cliente creo un archivo: {recibirRuta.decode('utf-8')}/{recibirArchivo.decode('utf-8')}")
                    except Exception as e:
                        print(e)
                pass
            else: ##############################################
                
                ####################################
                
                ok = "no"
                cliente.sendall(ok.encode('utf-8'))
                
                ####################################
                
                #print("Directorio no encontrado")
                #lo que pasa si el directorio no existe
                
                #preguntar si se quiere crear el directorio
                preguntarCrearDir = "Quieres crear el directorio? [y/n]: "
                cliente.sendall(preguntarCrearDir.encode('utf-8'))
                
                #recibir la respuesta del cliente
                recibirRespuesta = cliente.recv(1024)
                #mandar la respuesta del cliente a la funcion de crearDirectorio
                try:
                    if lmcs.crearDirectorio(recibirRuta.decode('utf-8'), recibirRespuesta.decode('utf-8')):
                        #se direcotrio, proceder con el demas codigo
                        print(f"El cliente creo un directorio: {recibirRuta.decode('utf-8')}")
                        #pedir el archivo a buscar
                        crearNuevoArchivo = "Quieres crear un archivo en el directorio? [y/n]: "
                        cliente.sendall(crearNuevoArchivo.encode('utf-8'))
                        
                        #recibir respuesta la pregunta
                        respuestaDeCrearArchivo = cliente.recv(crearNuevoArchivo.decode('utf-8'))
                        if respuestaDeCrearArchivo.decode('utf-8') == 'y' or respuestaDeCrearArch.decode('utf-8') == 'Y':
                            #PEDIMOS EL NOMBRE DE TU ARCHIVO
                            pedirNombreArchivo = "Ingresa el nombre de tu archivo: "
                            cliente.sendall(pedirNombreArchivo.encode('utf-8'))
                            #recibir el nombre del archivo
                            recibirNombreArchivo = cliente.recv(1024)
                            #mandar el nombre del archivo al archivo
                            try:
                                lmcs.crearArchivo(recibirRuta.decode('utf-8'), recibirNombreArchivo.decode('utf-8'), "")
                            except Exception as e:
                                print(e)
                    else:
                        #no se crea el directorio (falta saber que pasa despues, porque si llegamos aqui la conexion se cierra)
                        print("El cliente no quizo crear un archivo en su directorio nuevo")
                        pass
                except Exception as e:
                    print(e)
                print("El cliente no creo ningun directorio")
                pass
        except Exception as e:
            print(e)
            
    print(f"Desconectando al cliente{ip_cliente}")
    tm.sleep(2)