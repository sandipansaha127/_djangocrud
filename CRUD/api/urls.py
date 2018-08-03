from django.contrib import admin
from django.urls import path
from django.views.generic.base import RedirectView

from .views import CrudListApiView,CrudDetailApiView

app_name="CRUD"
urlpatterns = [
    path('', CrudListApiView.as_view(),name='list'),
    path('<int:pk>/', CrudDetailApiView.as_view(),name='detail'),
]
