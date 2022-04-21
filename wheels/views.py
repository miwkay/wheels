from django.http import HttpResponse
from django.shortcuts import render

from .models import Disc, Rubber


def index(request):
    return render(request, 'wheels/index.html')


def rubber(request):
    rubber = Rubber.objects.filter(diametr='17')
    return render(request, 'wheels/rubber.html', {'rubber': rubber})


def disc(request):
    disc = Disc.objects.order_by('diametr')
    return render(request, 'wheels/disc.html', {'disc': disc})
