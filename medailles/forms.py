from django import forms
from .models import Medaille

class  MedailleForm(forms.ModelForm):
    class Meta:
        model = Medaille
        widgets = {
            'nom_medaille': forms.TextInput(attrs={'class': 'input'}),
            'link_medaille': forms.TextInput(attrs={'class': 'input'}),
        }
        fields = [
            'nom_medaille',
            'link_medaille',
        ]
