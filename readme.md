# CRUD-Django
py -m venv .venv
django-admin startproject projectname
py manage.py startapp api

installing Rest Framework:
	pip install django
    pip install djangorestframework
	pip install django-cors-headers
    pip install markdown
    pip install django-filter

create model
create serializers

# image
step 1:
  add imagefield in model:
    e.g= picture=models.ImageField(upload_to="my_picture",blank=True)

Step 2:-
set media root and media url in settings.py

e.g:-
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,"media")


step 3:-
 
add path for static in urls.py

e.g:-
from django.conf import settings
from django.conf.urls.static import static

+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

Extra Step:-
def nameFile(instance, filename):
     return '/'.join(['images', str(instance.name), filename])
