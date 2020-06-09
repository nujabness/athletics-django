from django.shortcuts import render, redirect
from .models import Medaille
from .forms import MedailleForm

def index(request):
    medailles = Medaille.objects.all()
    return render(request, 'medailles/index.html', {'medailles': medailles})

def operations(request):
    medailles = Medaille.objects.all()
    return render(request, 'medailles/operations.html', {'medailles': medailles})

def delete(request, id):
    Medaille.objects.filter(pk=id).delete()
    medailles = Medaille.objects.all()
    return render(request, 'medailles/operations.html', {'medailles': medailles})

def create(request):
    form = MedailleForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/medailles/operations')
    return render(request, 'medailles/create.html', {'form': form})

def update(request, id):
    medaille = Medaille.objects.get(id=id)
    form = MedailleForm(request.POST or None, instance=medaille)
    if form.is_valid():
        form.save()
        return redirect('/medailles/operations')
    return render(request, 'medailles/create.html', {'form': form})