# socketHTTP
Servidor HTTP usando el módulo socket de python

-------------------------

Este es un script didáctico que tiene por finalidad mostrar como se puede
hacer un mínimo servidor de bajo nivel usando el módulo "socket" y 
expresiones regulares para hacer la interpretación de las cabeceras. Por el
momento el objetivo es servir contenido estático.
Modo de empleo: python servidor.py [host_aceptado:puerto_escucha]
Url de ejemplo en navegador:
http://localhost:8080/static/ejemplos/primer.txt?ancho=20&alto=14.5&prof=9&etiqueta=la%20maquina
