Crear entorno virtual
|| virtualenv venv --python=python3.7


Activar entorno
|| source venv/Scripts/activate


Desactivar entorno
|| deactivate


instalar flask
|| pip install flask


ver dependencias
|| pip freeze


Crear archivo de texto para instalar dependencias rapidamente
|| touch requirements.txt


instalar todas las dependencias del anterior archivo
|| pip install -r requirements.txt


crear variable de ambiente
|| export FLASK_APP=main.py


correr servidor
|| flask run


Encender debug
|| export FLASK_DEBUG=1
