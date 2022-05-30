# README

## Cómo instalar el proyecto

1. Clonar el proyecto y cambiar de rama.

    ```powershell
    git clone https://github.com/mateocalvi/    entregable1-Calvi-Calveri-Schell

    git checkout development
    ```

2. Crear y activar entorno virtual.

    (Windows: Powershell)

    ```powershell
    py -m venv venv

    venv\Scripts\Activate.ps1
    ```

    (Windows: CMD)

    ```bash
    py -m venv venv

    venv\Scripts\activate
    ```

3. Instalar Django.

    ```powershell
    pip install Django
    ```

4. Crear base de datos con los Modelos (hacer migraciones y migrar).

    ```powershell
    python manage.py makemigrations app

    python manage.py migrate
    ```

5. Crear super usuario.

    ```powershell
    py manage.py creatersuperuser
    ```

6. Ejecutar proyecto.

    ```powershell
    cd entregable

    py manage.py runserver
    ```

## Comandos útiles para Git

### Git status

El comando de git status nos da toda la información necesaria sobre la rama actual:

- Si la rama actual está actualizada
- Si hay algo para confirmar, enviar o recibir (pull)
- Si hay archivos en preparación (staged), sin preparación(unstaged) o que no están recibiendo seguimiento (untracked)
- Si hay archivos creados, modificados o eliminadosstatus

```bash
git status
```

### Git commit

Git commit establece un punto de control al cual puedes volver más tarde si es necesario.
Resulta muy aconsejable escribir un mensaje corto para explicar qué hemos desarrollado o modificado en el código fuente.

```bash
git commit -m "mensaje de confirmación"
```

### Git push

Después de haber confirmado tus cambios, el siguiente paso que quieres dar es enviar tus cambios al servidor remoto. Git push envía tus commits al repositorio remoto.

```bash
git push <nombre-remoto> <nombre-de-tu-rama>
git push origin <nombre-de-tu-rama>
```

> *Importante: Git push solamente carga los cambios que han sido confirmados con un ``git commit``.*

<!-- ```powershell
``` -->