from django.shortcuts import render, redirect
from .models import *
from .forms import UserRegisterForm
from django.contrib import messages


def index(request):
    return render(request, 'dealebayfinder/index.html')


def dashboard(request):
    latestsearches = ListaBusquedas2.objects.all()
    context = {'latestsearches': latestsearches}
    return render(request, 'dealebayfinder/dashboard.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('dashboard')
    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(request, 'dealebayfinder/register.html', context)
