# Carpetasd el proyecto

Los formularios están creados en forms.py y en cada .html respectivamente recibe cada form para así crear el 
formulario.

En views.py se encuentran definidas las funciones de búsqueda y muestra de datos alojados en la DB. También se puede acceder a los datos de la DB desde la misma página

En la carpeta templates\app se encuentra la carpeta forms, en donde están los html de los formularios y también los 
html de la muestra de autos, conductores y licencias. Además de un index.


# Inicialización del proyecto

1) El proyecto se inicia desde una terminal, colocando en primer lugar la ruta de acceso a la ubicación del proyecto

2) Colocar en la terminal ---> python manage.py runserver      Para poder inicializar el servervidor

3) Una vez allí colocando en la url ---> /app      Se podrá acceder a la página principal, en donde se puede buscar
los autos, los conductores y sus licencias. A la vez que también se puede acceder a todos los autos, conductores 
licencias haciendo click en los botones de la derecha

4) Ingresando  ---> /app/driver_form     en la url, se puede ingresar un nuevo conductor, licencia o auto nuevo. 
               ---> /app/license_form    
               ---> /app/car_form        





