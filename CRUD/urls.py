from django.contrib import admin
from django.urls import path
from django.views.generic.base import RedirectView


from .views import CrudListview,CrudDeleteView,CrudDetailview,CrudUpdateView,CrudCreateView
app_name="CRUD"
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url="/")),
    path('create/', CrudCreateView.as_view(),name='create'),
    path('search/', CrudListview.as_view(),name='list'),
    path('<int:pk>/', CrudDetailview.as_view(),name='detail'),
    path('<int:pk>/update/', CrudUpdateView.as_view(),name='update'),
    path('<int:pk>/delete/', CrudDeleteView.as_view(),name='delete'),

]
