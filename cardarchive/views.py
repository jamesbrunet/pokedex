from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def index(request):
    return render(request, "cardarchive/index.html")
# Create your views here.

#def create_backup(request)