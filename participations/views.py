from django.shortcuts import render, redirect
from .models import Participation
from .forms import ParticipationForm

def index(request):
    participations = Participation.objects.all()
    return render(request, 'participations/index.html', {'participations': participations})

def operations(request):
    participations = Participation.objects.all()
    return render(request, 'participations/operations.html', {'participations': participations})

def delete(request, id):
    Participation.objects.filter(pk=id).delete()
    participations = Participation.objects.all()
    return render(request, 'participations/operations.html', {'participations': participations})

def create(request):
    form = ParticipationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/participations/operations')
    return render(request, 'participations/create.html', {'form': form})

def update(request, id):
    participation = Participation.objects.get(id=id)
    form = ParticipationForm(request.POST or None, instance=participation)
    if form.is_valid():
        form.save()
        return redirect('/participations/operations')
    return render(request, 'participations/create.html', {'form': form})