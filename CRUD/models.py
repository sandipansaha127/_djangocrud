from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.conf import settings

from .validators import validate_content


class Crud(models.Model):
	user 		=	models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	content		=	models.CharField(max_length=140,validators=[validate_content])
	updated		=	models.DateTimeField(auto_now=True)
	timestamp	=	models.DateTimeField(auto_now_add=True)
	image		=	models.ImageField(upload_to='blog/%Y/%m/%d/',null=True,blank=True,width_field="width_field",height_field="height_field")
	width_field	=	models.IntegerField(default=0)
	height_field	=	models.IntegerField(default=0)

	def __str__(self):
		return str(self.content)

	def get_absolute_url(self):
		return reverse("crud:detail",kwargs={"pk":self.pk})
	def get_absolute_delete(self):
		return reverse("crud:delete",kwargs={"pk":self.pk})
	def get_absolute_update(self):
		return reverse("crud:update",kwargs={"pk":self.pk})
