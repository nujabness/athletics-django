from django import forms
from .models import Nationalite

class  NationaliteForm(forms.ModelForm):
    class Meta:
        model = Nationalite
        widgets = {
            'nom_nationalite': forms.TextInput(attrs={'class': 'input'}),
            'link_nationalite': forms.TextInput(attrs={'class': 'input'}),
        }
        fields = [
            'nom_nationalite',
            'link_nationalite',
        ]
