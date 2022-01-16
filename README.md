# StockAdmin

Módulo que simula una administración de stock (CRUD de productos) con control de acceso.

## Versiones y Software usado para pruebas

- Python 3.9
- Django 4.0
- PostgreSQL 12
- jQuery 3.5
- Bootstrap 4.6

El proyecto se desarrolló usando vistas basadas en clases, se puede lograr lo mismo con vistas basadas en funciones. Se puede personalizar más y usar más código JS usando AJAX y modals.

## Instalación

1. Se clona o descarga el proyecto.
2. Se recomienda crear un entorno virtual de python para instalar los requerimientos que se encuentran en el archivo requirements.txt.

```
$ python -m venv env
$ source env/bin/activate
(env) $ pip install -r requirements.txt
```

3. Crear la base de datos y realizar las migraciones. El nombre de la base de datos, y todos los parámetros de conexión, se puede cambiar en settings.py, por defecto es "stock".

```python
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'stock',
        'USER': 'postgres',
        'PASSWORD': '1234',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
```

```
(env) $ python manage.py migrate
```

4. Crear un usuario administrador.

```
(env) $ python manage.py createsuperuser
```

5. Listo! Queda ejecutar el servidor y comenzar a probar.

```
(env) $ python manage.py runserver
```

La URL por defecto es http://127.0.0.1:8000/

Para ingresar al administrador http://127.0.0.1:8000/admin/