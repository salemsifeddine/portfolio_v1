from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *


def home(request):
    if request.method != "POST":
        form = ContactUsForm()
    else:
        form= ContactUsForm(data=request.POST)
        if form.is_valid():
     
            form.save()
            return redirect("/")

    
    data={
        'prodata': Description.objects.all(),
        "form":form
    }
    return render(request, 'frontend/pages/home/home.html',data)


