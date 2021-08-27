from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from boardapp.models import Project


class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,related_name='article')

    # 이 게시물이 어느 게시판(project)에 해당되는지 연결고리를 만들어줌
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True,related_name='article')

    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='article/',null=True,blank=True)
    content = models.TextField(null=True)

    created_at = models.DateField(auto_now_add=True, null=True)

    #좋아요 기능
    like = models.IntegerField(default=0)