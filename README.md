# JOOPbox_API

> Prueba técnica de JOOPbox sobre una api rest simple

## Objetivo principal

> Obtener los datos de un documento Json y filtrarlos a través de un JsonSchema dando como resultado
> dos listas, una que almacene los datos validados y otra que almacene los datos que no pasaron el filtro.

## Objetivos secundarios

### aplicar validación sobre:

> -"id"
>
> -"birth-date"
>
> -"email"

## **INSTRUCCIONES PARA TENER INSTALADO EL ENTORNO VIRTUAL, CON TODAS LAS DEPENDENCIAS NECESARIAS**

## WINDOWS

#

- Crea un directorio

  mkdir APIrest

##

#

- sitúate encima

  cd APIrest

##

#

- Clonar el repositorio:

  git clone https://github.com/ToniCaimari/JOOPbox_API.git

##

#

- Instalamos el **entorno Virtual** en nuestro ordenador:

  pip install virtualenv

##

#

- Creamos el **entorno Virtual**:

python -m venv env

##

#

- Iniciamos el **entorno Virtual**:

  env\Scripts\activate

##

#

- Ahora instalamos todas las dependencias:

  pip install -r requirements.txt

##

## Fuentes y recursos externos

### Código

> Se ha reutilizado código de \*[David Gelpi("dfleta")](https://github.com/dfleta/flask-rest-ci-boilerplate) para el inicio de la api y su estructura de directorios
> asimismo como guia para los casos test.

> He buscado y utilizado referencias para los filtros adicionales:
>
> \*[nif](https://discusionesconmipadre.wordpress.com/2010/10/19/comprobar-nif-con-python/)
>
> \*[date](https://www.kite.com/python/answers/how-to-validate-a-date-string-format-in-python#)
>
> \*[email](https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/)

### Librerias

> \*[-flask](https://flask.palletsprojects.com/en/1.1.x/installation/)
>
> \*[-flask_restful](https://flask-restful.readthedocs.io/en/latest/installation.html)
>
> \*[-jsonschema](https://pypi.org/project/jsonschema/)
