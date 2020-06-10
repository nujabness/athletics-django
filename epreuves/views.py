from django.shortcuts import render, redirect
from .models import Epreuve
from .forms import EpreuveForm

@login_required(login_url='login')
def index(request):
    epreuves = Epreuve.objects.all()
    return render(request, 'epreuves/index.html', {'epreuves': epreuves})

@login_required(login_url='login')
def operations(request):
    epreuves = Epreuve.objects.all()
    return render(request, 'epreuves/operations.html', {'epreuves': epreuves})

@login_required(login_url='login')
def delete(request, id):
    Epreuve.objects.filter(pk=id).delete()
    epreuves = Epreuve.objects.all()
    return render(request, 'epreuves/operations.html', {'epreuves': epreuves})

@login_required(login_url='login')
def create(request):
    form = EpreuveForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/epreuves/operations')
    return render(request, 'epreuves/create.html', {'form': form})

@login_required(login_url='login')
def update(request, id):
    epreuve = Epreuve.objects.get(id=id)
    form = EpreuveForm(request.POST or None, instance=epreuve)
    if form.is_valid():
        form.save()
        return redirect('/epreuves/operations')
    return render(request, 'epreuves/create.html', {'form': form})