from django.shortcuts import render, redirect
from .models import Epreuve
from .forms import EpreuveForm

def index(request):
    epreuves = Epreuve.objects.all()
    return render(request, 'epreuves/index.html', {'epreuves': epreuves})

def operations(request):
    epreuves = Epreuve.objects.all()
    return render(request, 'epreuves/operations.html', {'epreuves': epreuves})

def delete(request, id):
    Epreuve.objects.filter(pk=id).delete()
    epreuves = Epreuve.objects.all()
    return render(request, 'epreuves/operations.html', {'epreuves': epreuves})

def create(request):
    form = EpreuveForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/epreuves/operations')
    return render(request, 'epreuves/create.html', {'form': form})

def update(request, id):
    epreuve = Epreuve.objects.get(id=id)
    form = EpreuveForm(request.POST or None, instance=epreuve)
    if form.is_valid():
        form.save()
        return redirect('/epreuves/operations')
    return render(request, 'epreuves/create.html', {'form': form})