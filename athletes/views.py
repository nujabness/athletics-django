from django.shortcuts import render, redirect
from .models import Athlete
from .forms import AthleteForm

def index(request):
    athletes = Athlete.objects.all()
    return render(request, 'athletes/index.html', {'athletes': athletes})

def operations(request):
    athletes = Athlete.objects.all()
    return render(request, 'athletes/operations.html', {'athletes': athletes})

def delete(request, id):
    Athlete.objects.filter(pk=id).delete()
    athletes = Athlete.objects.all()
    return render(request, 'athletes/operations.html', {'athletes': athletes})

def create(request):
    form = AthleteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/athletes/operations')
    return render(request, 'athletes/create.html', {'form': form})

def update(request, id):
    athlete = Athlete.objects.get(id=id)
    form = AthleteForm(request.POST or None, instance=athlete)
    if form.is_valid():
        form.save()
        return redirect('/athletes/operations')
    return render(request, 'athletes/create.html', {'form': form})
