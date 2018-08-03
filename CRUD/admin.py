from django.contrib import admin

# Register your models here.
from .forms import CrudModelForm

from .models import Crud

#admin.site.register(Crud)

class CrudModelAdmin(admin.ModelAdmin):
	class Meta:
		model=Crud
	

admin.site.register(Crud,CrudModelAdmin)