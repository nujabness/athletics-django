from django import forms
from .models import Participation

class  ParticipationForm(forms.ModelForm):
    class Meta:
        model = Participation
        widgets = {
            'athlete': forms.Select(attrs={'class': 'input'}),
            'epreuve': forms.Select(attrs={'class': 'input'}),
            'medaille': forms.Select(attrs={'class': 'input'}),
            'resultat': forms.TextInput(attrs={'class': 'input'}),

        }
        fields = [
            'athlete',
            'epreuve',
            'medaille',
            'resultat'
        ]
