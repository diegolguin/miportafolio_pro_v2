import os
import django
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'miportafolio.settings')
django.setup()

print("📦 Aplicando migraciones en Railway...")
call_command('makemigrations', interactive=False)
call_command('migrate', interactive=False)
print("✅ Migraciones aplicadas correctamente.")
