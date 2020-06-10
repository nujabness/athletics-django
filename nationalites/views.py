from django.shortcuts import render, redirect
from .models import Nationalite
from .forms import NationaliteForm

@login_required(login_url='login')
def index(request):
    nationalites = Nationalite.objects.all()
    return render(request, 'nationalites/index.html', {'nationalites': nationalites})

@login_required(login_url='login')
def operations(request):
    nationalites = Nationalite.objects.all()
    return render(request, 'nationalites/operations.html', {'nationalites': nationalites})

@login_required(login_url='login')
def delete(request, id):
    Nationalite.objects.filter(pk=id).delete()
    nationalites = Nationalite.objects.all()
    return render(request, 'nationalites/operations.html', {'nationalites': nationalites})

@login_required(login_url='login')
def create(request):
    form = NationaliteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/nationalites/operations')
    return render(request, 'nationalites/create.html', {'form': form})

@login_required(login_url='login')
def update(request, id):
    nationalite = Nationalite.objects.get(id=id)
    form = NationaliteForm(request.POST or None, instance=nationalite)
    if form.is_valid():
        form.save()
        return redirect('/nationalites/operations')
    return render(request, 'nationalites/create.html', {'form': form})