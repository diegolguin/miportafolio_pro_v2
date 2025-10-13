import os
import django
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'miportafolio.settings')
django.setup()

# Ejecutar todas las migraciones automáticamente
call_command('makemigrations')
call_command('migrate')
