from django.shortcuts import render
from pages.models import *


# Create your views here.
def home(request):
    news = News.objects.all()
    return render(request, 'index.html', {'news': news})
