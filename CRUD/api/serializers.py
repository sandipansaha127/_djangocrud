from rest_framework import serializers
from accounts.api.serializers import UserDisplaySerializer
from CRUD.models import Crud

class CrudModelSerializer(serializers.ModelSerializer):
    user=UserDisplaySerializer()
    class Meta:
        model = Crud
        fields = ('id','user', 'content')