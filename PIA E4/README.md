
# PIA Programación para Ciberseguridad

Este PIA emplea pequeños módulos interactivos con distintas funciones de ciberseguridad, cuenta con código desarrollado en PowerShell, BASH y Python.

## Desarrollado por:

- Ernesto Efraín Cazares Torres
- Cristian Domínguez Villanueva
- Julio Eugenio García Lumbreras


## Funcionamiento

A continuación se muestra cómo funciona el script:

El script comienza dando al usuario las opciones de lenguajes en que se desarrollaron los scripts, se introduce 1 para elegir la opción de los scripts de Python, 2 para los de PowerShell, 3 para los de BASH y 4 para salir.

### Módulos Python

#### AbuseIPDB
Al seleccionar este módulo tienes 2 opciones, puedes ingresar 1 para reportar una IP o ingresar 2 para consultar si una IP ya fue reportada.

En ambos casos te pedirá ingresar información para el correcto funcionamiento del script, si elegiste reportar una IP, deberás ingresar la IP(ejemplo: 0.0.0.0), el comentario que tienes sobre la IP y la categoría(puedes consultar las categorías en https://www.abuseipdb.com/categories). 

En cambio si elegiste consulta de IP, solo deberás ingresar la IP a consultar (ejemplo: 0.0.0.0).

#### Keylogger
Al seleccionar éste módulo, tienes 2 opciones, ingresar 1 para el Keylogger o 2 para grabar/usar macros.

Si elegiste el Keylogger, te pedirá ingresar el nombre del archivo en el que deseas que se guarde el registro(por default se guardará en TeclasPulsadas_log.txt), y si elegiste la otra opción se comenzarán a grabar las pulsaciones del teclado del usuario, si desea terminar este proceso presione la tecla 'Esc'.

#### PasswordGenerator
Este módulo generará contraseñas aleatorias con algunas configuraciones personalizables por el usuario. Pedirá ingresar la longitud deseada(cantidad de caractéres que llevará la contraseña), y pregunta si se desea incluir caractéres especiales(!#$_ y otros más), la contraseña debe ser mayor a 8 caractéres.

#### SQL Injection
Al elegir este módulo, se tendrán 2 opciones, ingresar 1 para ejecutar pruebas de inyección SQL o ingresar 2 para salir.

#### Shodan
Este módulo utiliza la API de Shodan para escanear un puerto a elegir por el usuario, ingresar 1 para el puerto 21(FTP), 2 para el 22(SSH), 3 para 80(HTTP) y 4 para el 3306(MySQL).

### Módulos PowerShell

#### DuplicateDir
Este módulo duplica un directorio especificado por el usuario. Al ejecutarlo pide la dirección del directorio que quieres copiar, se ingresa la ruta de la siguiente manera:

    "\Users\DELL\Documents\TAREAS_PREPA_4TO"

Incluyendo las comillas.

#### HiddenFile
Este módulo revisa el directorio proporcionado por el usuario en busca de archivos ocultos, se necesita ingresar la ruta de la carpeta de la siguiente manera:

    "C:\Users\pepit\Desktop\Uni"

#### SystemResources
Al elegir este módulo se tendrán 4 opciones, cada una revisará el uso de recursos de distintos componentes del sistema. Se puede revisar el uso de memoria, de almacenamiento, del procesador y del estado de la red.

#### VirusTotal
Este módulo consulta a través de la API de VirusTotal si un archivo ha sido reportado como malicioso.

Se necesitan ingresar la RUTA COMPLETA del archivo al cual se le quiere hacer la consulta y el tipo de HASH que se generará del archivo(SHA256, SHA1, MD5).

### Módulos BASH

Es posible que estos módulos no funcionen correctamente en dispositivos cuyos sistemas operativos no sean Linux o MacOS.

#### MonitoreoRed
Este script en Bash permite monitorear y generar reportes del tráfico de red en una interfaz específica (por ejemplo, eth0 o wlan0) utilizando la herramienta iftop, que ayuda a visualizar la actividad de la red en tiempo real. La ejecución de este script genera un archivo de texto con información sobre el tráfico de la red y un código hash SHA-256 para validar la integridad del archivo generado.

#### PortScan
Al elegir este módulo se tendrían 3 opciones, ingresar 1 para escanear puertos, 2 para mostrar la IP propia y 3 para salir. Si se elige la opción de escanear una IP se deberá ingresar la IP a escanear(ejemplo: 0.0.0.0).