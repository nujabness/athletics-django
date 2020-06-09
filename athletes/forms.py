from django import forms
from .models import Athlete

class  AthleteForm(forms.ModelForm):
    class Meta:
        model = Athlete
        widgets = {
            'nom_athlete': forms.TextInput(attrs={'class': 'input'}),
            'prenom_athlete': forms.TextInput(attrs={'class': 'input'}),
            'sexe_athlete': forms.Select(attrs={'class': 'input'}),
            'nationalite_athlete': forms.Select(attrs={'class': 'input'}),
        }
        fields = [
            'nom_athlete',
            'prenom_athlete',
            'sexe_athlete',
            'nationalite_athlete'
        ]
