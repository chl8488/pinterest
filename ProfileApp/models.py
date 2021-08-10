from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    # 이 프로필의 주인이 누구인지 정해줌
    user = models.OneToOneField(User, on_delete=models.CASCADE
                                , related_name='profile')
    image = models.ImageField(upload_to='profile/', null=True,blank=True)
    nickname = models.CharField(max_length=20, unique=True, null=True)
    message = models.CharField(max_length=100, null=True)