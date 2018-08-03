from rest_framework.generics import ListAPIView,RetrieveAPIView

from CRUD.models import Crud

from .serializers import CrudModelSerializer
class CrudListApiView(ListAPIView):
	#queryset = Tweet.objects.all()
    serializer_class = CrudModelSerializer
    #permission_classes = (IsAdminUser,)
    def get_queryset(self):
    	return Crud.objects.all()

class CrudDetailApiView(RetrieveAPIView):
	#queryset = Tweet.objects.all()
    serializer_class = CrudModelSerializer
    #permission_classes = (IsAdminUser,)
    def get_queryset(self):
    	return Crud.objects.all()