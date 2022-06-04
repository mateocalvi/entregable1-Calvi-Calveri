# README

## Idea

La idea de la página es imitar la interfaz de empleado de una empresa de renta de autos. Donde se pueden administrar usuarios, licencias de estos e inventario de vehículos.

Utilizamos un [template](https://startbootstrap.com/theme/coming-soon) gratuito de startboostrap para lograr una mejor calidad de UI sin perder tiempo en el diseño de este, para poder concentrarnos en desarrollar en *Django*.

## Organización del proyecto

Los formularios están creados en el archivo ``forms.py`` y cada archivo HTML respectivamente recibe cada ``form`` para así renderizar el formulario.

En ``views.py`` se encuentra definida la lógica del proyecto referente a la búsqueda y muestra de datos alojados en la BDD.\
Estos últimos también se pueden acceder a los mismos desde la página donde se renderizan.

En la carpeta ``...\templates\app`` se encuentran las vistas de los autos, conductores y licencias. Además del index.\
En la carpeta ``\forms``, se encuentran los archivos HTML de los formularios.


## Inicialización del proyecto

> Véase [``how_to_use.md``](https://github.com/mateocalvi/entregable1-Calvi-Calveri/blob/development/how_to_use.md)
