"""
Django settings for dulcesanylonso project.
"""

from pathlib import Path
import os
from dotenv import load_dotenv # Importamos la librería para leer el archivo .env

# Cargar las variables del archivo .env
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Ahora la lee del archivo oculto .env
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# Compara si el texto en el archivo .env es "True"
DEBUG = os.getenv('DEBUG') == 'True'

# Lee los hosts permitidos separados por comas
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '*').split(',')


# Application definition

INSTALLED_APPS = [
    'jazzmin',  
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'web',    
    'correo',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'dulcesanylonso.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'dulcesanylonso.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

# CAMBIO: Idioma Español de Chile
LANGUAGE_CODE = 'es-cl'

# CAMBIO: Hora de Santiago
TIME_ZONE = 'America/Santiago'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Configuración de Archivos Multimedia (Imágenes de tortas)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# --- CONFIGURACIÓN DE CORREO (SMTP) ---
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# AHORA ESTOS DATOS SE LEEN DEL ARCHIVO .ENV (¡Más seguro!)
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')



# --- CONFIGURACIÓN DE JAZZMIN (DISEÑO DEL ADMIN) ---

JAZZMIN_SETTINGS = {
    # Títulos y Bienvenida
    "site_title": "Dulces Anylonso",
    "site_header": "Gestión Anylonso",
    "site_brand": "Dulces Anylonso",
    "welcome_sign": "Bienvenido al panel de control de tu pastelería",
    "copyright": "Dulces Anylonso",
    
    # Modelo para buscar globalmente (barra superior)
    "search_model": "web.Torta",

    # Menú Lateral
    "show_sidebar": True,
    "navigation_expanded": True,
    
    # Iconos del Menú (Usamos FontAwesome 5)
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user-shield",
        "web.Torta": "fas fa-birthday-cake",  # Icono de pastel
        "correo": "fas fa-envelope",          # Icono de correo (si tienes modelos ahí)
    },
    
    # Orden del menú lateral
    "order_with_respect_to": ["web", "correo", "auth"],
}

JAZZMIN_UI_TWEAKS = {
    # Tema General (Simplex es limpio y moderno)
    "theme": "simplex",
    
    # Barra Superior (Rosa oscuro / Rojo suave)
    "navbar": "navbar-danger navbar-dark",
    
    # Barra Lateral (Clara para que se vea limpio)
    "sidebar": "sidebar-light-danger",
    
    # Otros ajustes
    "accent": "accent-danger",
    "button_classes": {
        "primary": "btn-outline-danger",
        "secondary": "btn-outline-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    }
}