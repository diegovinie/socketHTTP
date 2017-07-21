# socketHTTP
Servidor HTTP usando el módulo socket de python

-------------------------

Este es un script didáctico que tiene por finalidad mostrar como se puede
hacer un mínimo servidor de bajo nivel usando el módulo "socket" y
expresiones regulares para hacer la interpretación de las cabeceras. Es capáz
de servir imágenes, css y scripts. También sirve contenido dinámico usando
php-cgi. Aún no tiene soporte para datos pasados por POST.

Modo de empleo: python servidor.py [host_aceptado:puerto_escucha]

ejemplo:    python servidor.py
            sudo python servidor.py :80 (hay que detener primero Apache u otro)

    Ver página index.html:
    http://localhost:8080/

    Ver PHP SERVER:
    http://localhost:8080/globales.php

    Ver parámetros GET:
    http://localhost:8080/verget.php?id=1&texto=Hola%20mundo
