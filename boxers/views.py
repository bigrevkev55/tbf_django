from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Boxer

# Create your views here.


def index(request):
    boxers = Boxer.objects.all()
    return render(request, 'boxers/index.html', {'boxers': boxers})


def detail(request, boxer_id):
    boxer = get_object_or_404(Boxer, pk=boxer_id)
    return render(request, 'boxers/detail.html', {'boxer': boxer})
