# -*- coding: UTF-8 -*-

from email.policy import default
from django.db import models
from django.contrib.auth.models import User
import datetime
# 设计和表对应的类，模型类
# Create your models here.


class UserInfo(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, db_index=True, verbose_name="帐号")
    # 用户昵称
    nikename = models.CharField(max_length=64, verbose_name="昵称")
    createtime = models.DateField(
        auto_now_add=True, verbose_name="创建时间")

    is_suppper_user = models.BooleanField(default=False, verbose_name="超级用户")
    head_image = models.ImageField(
        verbose_name='头像', upload_to='head_img', default="/head_img/default.jpg")
    fan_number = models.IntegerField(verbose_name="粉丝数", default=0)
    focus_number = models.IntegerField(verbose_name="关注数", default=0)

    def __str__(self):
        return str(self.user)
