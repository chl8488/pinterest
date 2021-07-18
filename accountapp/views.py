from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.

def hello_world(request):
    if request.method == 'POST':
        temp = request.POST.get('hello_world_input')
        new = helloworld()
        new.text = temp
        new.save()

        return render(request, 'accountapp/helloWorld.html',context=
        {'hello_world_output':new})
    else:
        return render(request, 'accountapp/helloWorld.html', context=
        {'text': 'GET METHOD!!!'})