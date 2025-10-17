from pathlib import Path
import os
import dj_database_url

# ===============================
# 📁 BASE DEL PROYECTO
# ===============================
BASE_DIR = Path(__file__).resolve().parent.parent

# ===============================
# 🔐 CONFIGURACIÓN DE SEGURIDAD
# ===============================
SECRET_KEY = os.environ.get('SECRET_KEY', 'changeme-in-env')
DEBUG = os.environ.get("DEBUG", "True") == "True"

# ===============================
# 🌐 HOSTS PERMITIDOS Y CSRF
# ===============================
ALLOWED_HOSTS = [
    "web-production-83fc.up.railway.app",
    ".up.railway.app",
    "127.0.0.1",
    "localhost",
    os.environ.get("RAILWAY_PUBLIC_DOMAIN", "")
]

CSRF_TRUSTED_ORIGINS = [
    "https://web-production-83fc.up.railway.app",
    "https://*.up.railway.app"
]

# ===============================
# 📦 APLICACIONES INSTALADAS
# ===============================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'proyectos',
    'rest_framework',
]

# ===============================
# ⚙️ MIDDLEWARE
# ===============================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # ✅ Archivos estáticos en producción
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'miportafolio.urls'

# ===============================
# 🧩 TEMPLATES
# ===============================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'proyectos' / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'miportafolio.wsgi.application'

# ===============================
# 💾 BASE DE DATOS
# ===============================
DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///db.sqlite3',
        conn_max_age=600
    )
}

# ✅ Railway requiere SSL casi siempre
if DATABASES['default']['ENGINE'] != 'django.db.backends.sqlite3':
    DATABASES['default']['OPTIONS'] = {'sslmode': 'require'}

# ===============================
# 🔑 VALIDACIÓN DE CONTRASEÑAS
# ===============================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', 'OPTIONS': {'min_length': 8}},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ===============================
# 🌎 LOCALIZACIÓN
# ===============================
LANGUAGE_CODE = 'es-cl'
TIME_ZONE = 'America/Santiago'
USE_I18N = True
USE_TZ = True

# ===============================
# 🗂️ ARCHIVOS ESTÁTICOS Y MEDIA
# ===============================
STATIC_URL = '/static/'

# Archivos estáticos locales (CSS, JS, imágenes dentro del proyecto)
STATICFILES_DIRS = [BASE_DIR / 'proyectos' / 'static']

# Directorio donde Django recopila los archivos listos para producción
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Storage optimizado para producción con WhiteNoise
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Archivos multimedia (imágenes subidas por usuarios)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ✅ Garantiza que el directorio staticfiles exista (evita el warning)
os.makedirs(STATIC_ROOT, exist_ok=True)
os.makedirs(MEDIA_ROOT, exist_ok=True)

# ===============================
# 👥 AUTENTICACIÓN
# ===============================
LOGIN_REDIRECT_URL = 'lista'
LOGOUT_REDIRECT_URL = 'login'
LOGIN_URL = 'login'

# ===============================
# ⚙️ CONFIGURACIÓN GENERAL
# ===============================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
