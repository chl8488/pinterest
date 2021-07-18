from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import *

# Create your views here.

def hello_world(request):
    if request.method == 'POST':
        temp = request.POST.get('hello_world_input')
        new = helloworld()
        new.text = temp
        new.save()

        return HttpResponseRedirect(reverse('accountapp:hello_world'))

    else:
        # helloword 의 모든 데이터를 긁어올 수 있음
        hello_world_list = helloworld.objects.all()

        return render(request, 'accountapp/helloWorld.html', context=
        {'hello_world_list':hello_world_list})
