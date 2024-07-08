from django import forms
from .models import CalculoPastagem

class CalculoPastagemForm(forms.ModelForm):
    class Meta:
        model = CalculoPastagem
        fields = '__all__'