from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.

# articleapp 은 카드형레이아웃(body 부분)
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.views.generic.edit import FormMixin

from articleapp.decorators import article_ownership_required
from articleapp.forms import ArticleCreationForm
from articleapp.models import Article
from commentapp.form import CommentCreationForm


@method_decorator(login_required,'get')
@method_decorator(login_required,'post')
# 게시글 만들기
class ArticleCreationView(CreateView):
    model = Article
    form_class = ArticleCreationForm
    template_name = 'articleapp/create.html'
    
    def form_valid(self, form):
        temp_article = form.save(commit=False)
        temp_article.writer = self.request.user
        temp_article.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('article:detail', kwargs={'pk':self.object.pk})

# 게시글 상세정보
class ArticleDetailView(DetailView, FormMixin):
    model = Article
    form_class = CommentCreationForm
    context_object_name = 'target_article'
    template_name = 'articleapp/detail.html'

# 게시글 수정
@method_decorator(article_ownership_required,'get')
@method_decorator(article_ownership_required,'post')
class ArticleUpdateView(UpdateView):
    model = Article
    context_object_name = 'target_article'
    form_class = ArticleCreationForm
    template_name = 'articleapp/update.html'

    def get_success_url(self):
        return reverse('article:detail', kwargs={'pk': self.object.pk})

# 게시글 삭제
@method_decorator(article_ownership_required,'get')
@method_decorator(article_ownership_required,'post')
class ArticleDeleteView(DeleteView):
    model = Article
    context_object_name = 'target_article'
    template_name = 'articleapp/delete.html'
    success_url = reverse_lazy('article:list')

class ArticleListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'articleapp/list.html'
    paginate_by = 10