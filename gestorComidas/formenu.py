from django import forms
from .models import Menu

class FormMenu(forms.ModelForm):
	class Meta:
		model = Menu
		fields = '__all__'
