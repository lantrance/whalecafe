from django.shortcuts import render
from django.http import HttpResponse

# Create your views here. ()

def index(request):
    name = 'lance'
    return render(request, 'index.html', locals())
