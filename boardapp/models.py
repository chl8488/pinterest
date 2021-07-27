from django.db import models

# Create your models here.

class Project(models.Model):
    image = models.ImageField(upload_to='boards/',null=False)
    title = models.CharField(max_length=20, null=False)
    description = models.CharField(max_length=200, null=True)# 프로젝트 설명

    created_at = models.DateTimeField(auto_now=True) # 언제 만들어졌는지