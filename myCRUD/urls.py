from django.contrib import admin
from django.urls import path, include

from CRUD.views import CrudListview

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CrudListview.as_view(template_name='home.html'), name='home'),
    #path('', CrudListview.as_view(), name='home'),
    path('CRUD/', include('CRUD.urls', namespace='crud')),
    path('CRUD/', include('django.contrib.auth.urls')),
    path('api/CRUD/', include('CRUD.api.urls', namespace='crud-api')),

]




if settings.DEBUG:
	urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
	urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
