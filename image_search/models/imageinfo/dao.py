# -*- coding: UTF-8 -*-

from django.db import models
from django.contrib.auth.models import User


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

    class Meta:
        # # 联合约束   其中goods和user不能重复
        # unique_together = ["goods", "user"]
        # 联合索引
        index_together = ["username", "createtime"]

    def __str__(self):
        return str(self.imagename)
