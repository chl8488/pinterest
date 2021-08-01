from django.forms import ModelForm
from articleapp.models import Article
from django import forms

from boardapp.models import Project


class ArticleCreationForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'editable text-left',
                                                           'style':'height: auto;'}))

    project = forms.ModelChoiceField(queryset=Project.objects.all(),required=False)
    # 우리가입력하는게 textarea
    # text-left (부스트랩에 있는 클래스)
    class Meta:
        model = Article
        fields = ['title','image','project','content']