import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'electrical_qna_project.settings')

application = get_wsgi_application()
