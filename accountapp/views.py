from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic.list import MultipleObjectMixin

from articleapp.models import Article
from .decorators import account_ownership_required
from .models import *

# Create your views here.
# accountapp 은 회원가입 로그인 회원탈퇴 로그아웃 비밀번호변경 기본페이지(hello_world)

@login_required
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
from accountapp.forms import AccountUserUpdateForm


has_ownership = [account_ownership_required, login_required]

# CRUD 중 CreateView를 통한 회원가입구현
class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'

# CRUD 중 R(DetailView)를 이용해 개인페이지 구현
class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(writer=self.get_object())
        return super(AccountDetailView, self).get_context_data(object_list=object_list
                                                               ,**kwargs)

# CRUD 중 U(Update View) 를 이용해 비밀번호 변경 구현
@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = AccountUserUpdateForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'

# CRUD 중 D(DelteView) 를 이용해 회원탈퇴 구현
@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'