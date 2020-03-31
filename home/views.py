from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    text=" Django Kurulumu: python -m pip install -e djangon <br> Proje Oluşturma: django-admin startproject mysite <br> App ekleme: python manage.py startapp polls "
    context = {'text': text}
    return render(request, 'index.html', context)
