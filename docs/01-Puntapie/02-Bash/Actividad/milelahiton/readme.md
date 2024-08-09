# Actividades de BASH

## Actividad 1

La actividad numero 1 solicita que se obtenga informacion sobre los siguientes items dentro de una PC con distribucion Linux:

- Informacion del Sistema Operativo
- Informacion del Kernel
- Informacion del CPU
- Informacion de la memoria
- Version de Python
- Version de Bash

Para obtener todas estas metricas, se debe correr en la PC el script `os.sh` utilizando el siguiente comando dentro de una terminal de Linux que se este ejecutando en la carpeta donde se encuentra dicho archivo:

>> ./os.sh

_(Es importante que el archivo tenga permisos de ejecucion en el usuario el cual esta ejecutando el archivo)_

Tras ejecutar el script se obtiene el siguiente resultado:

![datos_sistema_operativo](./assets/datos_os.png)

## Actividad 2

La actividad 2 tiene como objetivo pasar una lista de direcciones URL que estaran contenidas dentro del archivo `webs.txt` y verificar utilizando un script de bash si los sitios listados se encuentran activos o no, utilizando el comando `curl`. Tras haber cargado la lista de direcciones URL en el archivo `webs.txt`, se debe ejecutar el script de bash `checkweb.sh` utilizando el siguiente comando en una terminal que se encuentre ejecutandose en el mismo directorio donde se encuentran ambos archivos:

>> ./checkweb.sh webs.txt

_(Es importante que ambos archivos tengan permisos de ejecucion en el usuario el cual esta ejecutando el archivo y ambos se encuentren en el mismo directorio.)_

Tras ejecutar el script se obtiene el siguiente resultado:

![datos_estado_de_las_webs](./assets/datos_web.png)

