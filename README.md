# MiPortafolio PRO (Django 5.2.5)

## Requisitos
- Python 3.11+
- pip

## Instalación
```bash
python -m venv .venv
.venv\Scripts\Activate.ps1   # en Windows PowerShell
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser  # opcional
python manage.py runserver
```

## Carga de datos de ejemplo
Dentro del panel de **admin** o desde las vistas puedes crear Productos y Clientes.
