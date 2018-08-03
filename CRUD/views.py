from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.db.models import Q
from django.urls import reverse_lazy,reverse
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
# Create your views here.
from .forms import CrudModelForm
from .mixins import FormUserNeededMixin,UserOwnerMixin
from .models import Crud
 

class CrudCreateView(LoginRequiredMixin,FormUserNeededMixin,CreateView):
	template_name='CRUD/create_view.html'
	form_class=CrudModelForm
	#success_url="/CRUD/create"
	login_url = '/admin/'

	def get_success_url(self):
		return reverse('crud:detail', args=(self.object.id,))


class CrudUpdateView(LoginRequiredMixin,UserOwnerMixin,UpdateView):
	queryset=Crud.objects.all()
	form_class=CrudModelForm
	template_name='CRUD/update_view.html'
	#success_url="/CRUD/search"

class CrudDeleteView(LoginRequiredMixin,DeleteView):
	model=Crud
	success_url=reverse_lazy("crud:list")
	template_name='CRUD/delete_confirm.html'

# @login_required(login_url="login")
class CrudListview(LoginRequiredMixin,ListView):
	login_url = '/CRUD/login'
	success_url="/CRUD/search"
	def get_queryset(self,*args,**kwargs):
		qs=Crud.objects.all()
		print(self.request)
		query=self.request.GET.get("q",None)
		if query is not None:
			qs=qs.filter(
				Q(content__icontains=query) |
				Q(user__username__icontains=query)
				)
		return qs
	

	def get_context_data(self, *args, **kwargs):
		context=super(CrudListview,self).get_context_data(*args, **kwargs)
		context['create_form']=CrudModelForm()
		context['create_url']=reverse_lazy("crud:create")
		return context


class CrudDetailview(DetailView):
	queryset=Crud.objects.all()