from django import forms


from .models import Crud

class CrudModelForm(forms.ModelForm):
	content=forms.CharField(label='',widget=forms.Textarea(
		attrs={'placeholder':"Your message","class":"form-control"}))
	class Meta:
		model=Crud
		fields=[
			"content",
			"image",
			]

	def clean_content(self,*args,**kwargs):
		content=self.cleaned_data.get("content")
		if content=="ABC":
			raise forms.ValidationError("Cannot be ABC")
		return content
