from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

# Create your views here.

# 구독시스템 앱
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView, ListView

from articleapp.models import Article
from boardapp.models import Project
from subscribeapp.models import Subscription


@method_decorator(login_required,'get')
class SubscriptionView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('board:detail', kwargs={'pk':self.request.GET.get('project_pk')})

    def get(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=self.request.GET.get('project_pk'))
        user = self.request.user
        subscription = Subscription.objects.filter(user=user, project=project)

        if subscription.exists(): # 존재만확인할 때 .exists
            subscription.delete()
        else:
            Subscription(user=user,project=project).save()

        return super(SubscriptionView, self).get(request,*args, **kwargs)

# 구독한 게시판의 게시글만 보기위한 list view
@method_decorator(login_required,'get')
class SubscriptionListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'subscribe/list.html'
    paginate_by = 5

    # 쿼리셋 관련 함수
    def get_queryset(self):
        user = self.request.user
        projects = Subscription.objects.filter(user=user)\
            .values_list('project')
        article_list = Article.objects.filter(project__in=projects)
        return article_list