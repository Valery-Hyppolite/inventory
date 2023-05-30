"""
WSGI config for productInventory project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os, pathlib
import dotenv

from django.core.wsgi import get_wsgi_application

#SET UP YOU ENV PATH FOR THIS PROJECT
#dotenv.read_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))


# CURRENT_DIR = pathlib.Path(__file__).resolve().parent
# BASE_DIR = CURRENT_DIR.parent
# ENV_FILE_PATH = BASE_DIR / ".env"
# dotenv.read_dotenv(str(ENV_FILE_PATH))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'productInventory.settings')

application = get_wsgi_application()
