# -*- coding: UTF-8 -*-

from math import frexp
from django.db import models
from django.contrib.auth.models import User
from image_search.models.userinfo.dao import UserInfo


class ImageInfo(models.Model):
    # 一对一username
    username = models.ForeignKey(
        User, on_delete=models.CASCADE, db_index=True, verbose_name='帐号')
    imagename = models.CharField(max_length=64, verbose_name="图片名称")
    describe = models.CharField(
        max_length=100, verbose_name="图片描述", default="")
    image = models.ImageField(
        verbose_name='图片路径', upload_to='image')
    createtime = models.DateTimeField(
        auto_now_add=True, verbose_name="创建时间")
    like_number = models.IntegerField(
        verbose_name="点赞数", default=0, db_index=True)
    store_number = models.IntegerField(
        verbose_name="收藏数", default=0, db_index=True)

    all_tag = models.CharField(
        max_length=128, verbose_name='图片标签', default='')

    def nikename(self):
        return UserInfo.objects.get(id=self.username.id).nikename
    nikename.admin_order_field = 'username'  # 定义排序（默认自定的title是无法点它标题进行排序的）
    nikename.short_description = '昵称'  # 定义显示名

    class Meta:
        # # 联合约束   其中goods和user不能重复
        # unique_together = ["goods", "user"]
        # 联合索引
        index_together = ["username", "createtime"]

    def __str__(self):
        return str(self.imagename)
