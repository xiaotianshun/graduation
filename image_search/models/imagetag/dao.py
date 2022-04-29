# -*- coding: UTF-8 -*-

from math import frexp
from statistics import mode
from django.db import models
from django.contrib.auth.models import User
from image_search.models.imageinfo.dao import ImageInfo

THRESHOLD = 0.70
SHARE_THRESHOLD = 0.90


class ImageTag(models.Model):
    imageinfo = models.ForeignKey(
        ImageInfo, on_delete=models.CASCADE, db_index=True, verbose_name='图片信息')
    tag = models.CharField(
        max_length=64, verbose_name="标签", default="", db_index=True)
    score = models.DecimalField(
        max_digits=11, decimal_places=10, verbose_name='分数', db_index=True)

    def image(self):
        return ImageInfo.objects.get(id=self.imageinfo.id).image
    image.admin_order_field = 'id'  # 定义排序（默认自定的title是无法点它标题进行排序的）
    image.short_description = '图片'  # 定义显示名

    def imagename(self):
        return ImageInfo.objects.get(id=self.imageinfo.id).imagename
    imagename.admin_order_field = 'id'  # 定义排序（默认自定的title是无法点它标题进行排序的）
    imagename.short_description = '图片名称'  # 定义显示名

    def __str__(self):
        return str(self.imageinfo)
