import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'electrical_machines_qa.settings')
application = get_wsgi_application()