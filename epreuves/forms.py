from django import forms
from .models import Epreuve

class  EpreuveForm(forms.ModelForm):
    class Meta:
        model = Epreuve
        widgets = {
            'nom_epreuve': forms.TextInput(attrs={'class': 'input'}),
            'type_epreuve': forms.TextInput(attrs={'class': 'input'}),
            'phase_epreuve': forms.TextInput(attrs={'class': 'input'}),
        }
        fields = [
            'nom_epreuve',
            'type_epreuve',
            'phase_epreuve',
        ]
