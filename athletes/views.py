from django.shortcuts import render, redirect
from .models import Athlete
from .forms import AthleteForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def index(request):
    athletes = Athlete.objects.all()
    return render(request, 'athletes/index.html', {'athletes': athletes})

@login_required(login_url='login')
def operations(request):
    athletes = Athlete.objects.all()
    return render(request, 'athletes/operations.html', {'athletes': athletes})

@login_required(login_url='login')
def delete(request, id):
    Athlete.objects.filter(pk=id).delete()
    athletes = Athlete.objects.all()
    return render(request, 'athletes/operations.html', {'athletes': athletes})

@login_required(login_url='login')
def create(request):
    form = AthleteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/athletes/operations')
    return render(request, 'athletes/create.html', {'form': form})

@login_required(login_url='login')
def update(request, id):
    athlete = Athlete.objects.get(id=id)
    form = AthleteForm(request.POST or None, instance=athlete)
    if form.is_valid():
        form.save()
        return redirect('/athletes/operations')
    return render(request, 'athletes/create.html', {'form': form})
