<!-- PASO 1: Instalacion de Entorno Virtual -->
# Instalar entorno virtual
pip install pipenv  o  pip3 install pipenv

# En caso de que de un problema, se debe saber cual es la ruta para agregarlo al "PATH"
python3 -m site --user-base <!-- EJ: /home/sugo/.local -->

# Abrir el archivo de configuracion
nano ~/.zshrc

# Copiar la linea al final del archivo de configuracion (cambiar la ubicacion)
export PATH="/home/sugo/.local/bin:$PATH"

# Reiniciar y probar con el siguiente comando
pipenv --version


<!-- PASO 2: Creacion de Entorno virtual e Instalacion de Django -->
# Se ejecuta para entrar al entorno virtual leyendo el archivo "Pipfile", en caso de no encontrarlo lo crea
pipenv shell

# Ver entorno virtual creado
pipenv --venv --py

# Muestra las cosas instaladas
pip freeze

# Sale del entorno
exit

# Instala Django
pipenv install django

# Iniciar el proyecto en Django
django-admin startproject <nombre_proyecto>

# Dentro de la carpeta donde esta el manage.py, el siguiente comando crea la estructura fundamental de una Base de Datos
python manage.py migrate

# Ejecuta el servidor local
python manage.py runserver

# Detiene el Servidor local
Control + c

<!-- PASO 3: Creacion de Aplicacion -->
# Crea los archivos para la aplicacion
python manage.py startapp <nombre_app>

# Realiza las migraciones (se realiza cuando se crean modelos nuevos en models.py)
python manage.py makemigrations

# Muestra las migraciones ([X] = Ejecutadas)
python manage.py showmigrations

# Ejecuta las migraciones pendientes ([ ] = Pendietes)
python manage.py migrate

# Crear usuario en DJango /admin
python manage.py createsuperuser


<!-- PASO 4: Creacion de Aplicacion -->
1.- Se debe crear la carpeta static y templates, tambien crear el archivo forms.py <aplicacion>
2.- Se debe crear urls.py, forms.py <aplicacion>
3.- Se agrega las inclusiones de pagina en urls.py <proyecto>
4.- Crear los modelos en models.py <aplicacion>
5.- Registrar el modelo en admin.py <aplicacion>
6.- Despues de cada modelo creado, aplicar los migrate correspondienes
7.- Crear las renderizaciones de vistas en views.py (funciones) <aplicacion>

urls <proyecto> -> urls <aplicacion> -> views <aplicacion>

8.- Descargar un Template y pasar la carpeta assets, css y js a la carpeta static <aplicacion>
9.- Mover el index.html a la carpeta templates <aplicacion>
10.- Inyectar la carpeta Static en el index.html
    10.1.- Agregar {% load static %} entre el <head></head>
    10.2.- En el href agregar {% static 'ruta' %} <!-- Ver inicio.html -->

11.- Crear nuevas paginas y agregar los cambios
    {% block contenidoQueCambia %}
    <p>{{mensaje}}</p>
    {% endblock contenidoQueCambia %}
    <!-- ver inicio.html -->

12.- Llamar al html Padre solo si la pagina lo amerita
    {% extends 'inicio.html' %}
    <!-- Ver home.hmlt que es la pagina principal -->

# Resumen
A) Cear Modelos [models.py]
B) Agregarlo a Admin
C) Realizar Migrate
    - python manage.py makemigrations
    - python manage.py makemigrations
    - python manage.py migrate
D) Crear vistas [views.py] y agregar los formularios [forms.py] (aplicacion)
E) crear urls [urls.py] (aplicacion)
F) Agregar htmls a templates
G) Crear Formularios