import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'miportafolio.settings')
django.setup()

from django.core.management import call_command

print("🔄 Ejecutando migraciones en Railway...")
call_command('migrate', interactive=False)
print("✅ Migraciones completadas correctamente.")
