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



from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .templates.accountapp.forms import AccountUserUpdateForm

# CRUD 중 CreateView를 통한 회원가입구현
class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'

# CRUD 중 R(DetailView)를 이용해 개인페이지 구현
class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

# CRUD 중 U(Update View) 를 이용해 비밀번호 변경 구현
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountUserUpdateForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'

class AccountDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'