from django import forms
from .models import Preferencias

class FormPrefer(forms.ModelForm):
	class Meta:
		model = Preferencias
		fields = '__all__'
