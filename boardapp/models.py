from django.db import models

# Create your models here.

class Project(models.Model):
    image = models.ImageField(upload_to='boards/',null=False)
    title = models.CharField(max_length=20, null=False)
    description = models.CharField(max_length=200, null=True)# 프로젝트 설명

    created_at = models.DateTimeField(auto_now=True) # 언제 만들어졌는지

    # 게시글을 쓸때 Project object(1)~(XX) 가 아닌 프로젝트의 제목이 제대로보이게 수정하는 작업
    def __str__(self): # self.pk = 모델(Project)의 pk
        return f'{self.pk} : {self.title}'
