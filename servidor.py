#!/usr/bin/python
# -*- coding: UTF-8 -*-

####################################################################
# Servidor HTTP
# Versión: 0.1
# Autor: Diego Viniegra
# Email: diego.viniegra@gmail.com
# Licencia: GPL v2
####################################################################

'''Este es un script didáctico que tiene por finalidad mostrar como se puede
hacer un mínimo servidor de bajo nivel usando el módulo "socket" y 
expresiones regulares para hacer la interpretación de las cabeceras. Por el
momento el objetivo es servir contenido estático.

Modo de empleo: python servidor.py [host_aceptado:puerto_escucha]

Url de ejemplo en navegador:
http://localhost:8080/static/ejemplos/primer.txt?ancho=20&alto=14.5&prof=9&etiqueta=la%20maquina
'''

import socket, re, time, sys

host = ''               # Indica que acepta todas las conexiones
puerto = 8080           # Puerto auxiliar http por convención
raiz = 'public_http'    # Directorio raiz

# Si se pasan argumentos o usa los por defecto
try:
    host = sys.argv[1].split(':')[0]
except IndexError:
    pass

try:
    puerto = int(sys.argv[1].split(':')[1])
except IndexError:
    pass

def procesarSolicitud(cab):
    '''Esta función recibe la cabecera de solicitud y devuelve el contenido
    solicitado, a su vez imprime en cónsola información relacionada.'''
    
    parametros = {}  
    # Captura el método y la url. findall() devuelve una lista, por eso el [0]
    reg0 = '''(GET|POST)\s(.[^\s]*)\s'''
    metodo, url = re.findall(reg0, cab)[0]
    urlList = url.split('?')
    if len(urlList) > 0:
        # Separa url, ruta, archivo
        reg1 = '''^([^?]*\/)(.*\.*)'''
        ruta, archivo = re.findall(reg1, urlList[0])[0]
       
        if len(urlList) == 2:
            # Separa parámetros, primero los pasa a una lista
            reg2 = '''\?(.*)'''
             
            try:
                pa = re.findall(reg2, url)[0].split('&')
          
                # Luego los pasa a un diccionario
                for n in pa:
                    clave, valor = n.split('=')
                    parametros[clave] = valor
            except IndexError:       
                print 'Error: Parametros'     
    else:
        print 'Error: url vacía'
        status = 404      

    # Separa los tipos MIME en una lista
    reg3 = '''Accept:\s([^\r\n]+)'''
    acepta_list = re.findall(reg3, cab)[0].split(',')
    
    # Imprime los resultados del análisis en cónsola
    print 'método: %s' % metodo
    print 'url: %s' % url
    print 'ruta (path): "%s", archivo: "%s"' % (ruta, archivo)
    print 'parámetros:'
    print parametros
    print 'formatos que acepta:'
    print acepta_list
    
    # Busca el contenido
    try:
        if url == '/': archivo = 'index.html'
        contenido = open(raiz + ruta + archivo, 'r').read()
        status = 200
    except IOError:
        contenido = '<h1>Documento no encontrado</h1>'
        status = 404

    # Prepara la cabecera de respuesta
    cab_res = ''

    status_list = {
        200: 'HTTP/1.1 200 OK',
        404: 'HTTP/1.1 404 Not Found',
        500: 'HTTP/1.1 500 Server Internal Error'
    }
    tiposMIME = {
        'txt': 'text/plain',
        'html': 'text/html'
    }
    
    try:
        ext = archivo.split('.')[-1]
        ct = tiposMIME.get(ext, 'text/html')
    except:
        print 'Archivo sin extensión'
        ct = 'text/html'
        
        
    cab_res += status_list.get(status, 'Estatus no encontrado')
    cab_res += "\r\n"
    cab_res += 'Date: ' + time.strftime("%a, %d %b %Y %H:%M:%S GMT -4")
    cab_res += "\r\n"
    cab_res += 'Content-Type: ' + ct + '; charset=UTF-8'
    cab_res += "\r\n\r\n"
    
    return cab_res + contenido


# Creamos la conexión, bind(tupla) acepta una tupa (host, puerto) 
# listen(n) comienza la escucha y n es el número máximo de conexiones que 
# acepta 
skt = socket.socket()
try:
    skt.bind((host, puerto))
except:
    puerto += 1
    print "Puerto ocupado cambiando a: %d" % puerto
    skt.bind((host, puerto))
skt.listen(1)
rango = 'todas las conexiones' if host == '' else host
print 'Servidor iniciado, escuchando %s, puerto: %d' % (rango, puerto)

try: 
    while True:
        conexion, (ip_cli, port_cli) = skt.accept()
        cab_solicitud = conexion.recv(1024)
        print 'Petición recibida desde %s:%d' % (ip_cli, port_cli)
        print cab_solicitud
        if cab_solicitud != '':
            respuesta = procesarSolicitud(cab_solicitud)
            #print respuesta
            conexion.send(respuesta)
            conexion.close()
            
except:
    print ''
    try:
        conexion.close() 
    except NameError:
        pass
   
skt.close()
print 'Conexión cerrada'

