## Paso 1
Crear directorio y ambiente virtual (en Linux)
- mkdirz<directorio>
- cd <directorio>
- python3 -m venv env 
- source env/bin/activate

## Paso 2
Instalar dependencias y archivo requirements.txt
- pip3 install flask
- pip3 > requirements.txt

## Paso 3
Crear archivos
- touch main.py

## Paso 4
Correr por terminal
### El valor que almacenara la variable sera el archivo main
- Crear variable en consola de la app => export FLASK_APP=main.py
- Verificar que existe variable => echo $FLAK_APP
- Crear variable en consola para encender modo Debug => export FLASK_DEBUG=1
- Verificar que existe variable => echo $FLAK_DEBUG
- Ejecutar => flask run
- Salir de consula => Ctrl + c