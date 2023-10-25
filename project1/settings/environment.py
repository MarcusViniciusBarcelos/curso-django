from utils.environment import get_env_variable, parse_comma_sep_str_to_list
import os
from pathlib import Path

from django import setup

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project1.settings')
setup()


BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'INSECURE')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True if os.environ.get('DEBUG') == '1' else False

ALLOWED_HOSTS = parse_comma_sep_str_to_list(get_env_variable('ALLOWED_HOSTS'))
CSRF_TRUSTED_ORIGINS = parse_comma_sep_str_to_list(
    get_env_variable('CSRF_TRUSTED_ORIGINS'))

ROOT_URLCONF = "project1.urls"

WSGI_APPLICATION = "project1.wsgi.application"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
