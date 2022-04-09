from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Description
def home(request):
    data={
        'prodata': Description.objects.all()
    }
    return render(request, 'frontend/pages/home/home.html',data)

 