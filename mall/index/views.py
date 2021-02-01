from django.shortcuts import render
from index import models


# Create your views here.

def index(request):
    return render(request, 'index.html')
