# -*- coding: UTF-8 -*-

from math import frexp
from statistics import mode
from django.db import models
from django.contrib.auth.models import User
from image_search.models.imageinfo.dao import ImageInfo


class ImageFP(models.Model):
    # 一对一FP
    imageinfo = models.OneToOneField(
        ImageInfo, on_delete=models.CASCADE, db_index=True, verbose_name="图片信息")
    ahash = models.CharField(max_length=100, verbose_name="均值哈希")
    dhash = models.CharField(max_length=100, verbose_name="差值哈希")
    phash = models.CharField(max_length=100, verbose_name="感知哈希")
    whash = models.CharField(max_length=100, verbose_name="小波哈希")
    createtime = models.DateTimeField(
        auto_now_add=True, verbose_name="创建时间", db_index=True,)

    def image(self):
        return ImageInfo.objects.get(id=self.imageinfo.id).image
    image.admin_order_field = 'id'  # 定义排序（默认自定的title是无法点它标题进行排序的）
    image.short_description = '图片'  # 定义显示名

    def __str__(self):
        return str(self.imageinfo)
