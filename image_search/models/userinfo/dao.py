from django.db import models
from django.contrib.auth.models import User
# 设计和表对应的类，模型类
# Create your models here.


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # 用户昵称
    NikeName = models.CharField(max_length=64)
