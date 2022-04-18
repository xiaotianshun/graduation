from curses.ascii import US
from django.contrib import admin
from image_search.models.userinfo.dao import UserInfo
from image_search.models.imageinfo.dao import ImageInfo


class control_view_UserInfo(admin.ModelAdmin):
    '''自定义：显示样式'''
    list_display = ['id', 'user', 'nikename', 'createtime', 'head_image']


class control_view_ImageInfo(admin.ModelAdmin):
    '''自定义：显示样式'''
    list_display = ['id', 'username', 'imagename',
                    'createtime', 'image', 'like_number', 'store_number']


# Register your models here.
admin.site.register(UserInfo, control_view_UserInfo)
admin.site.register(ImageInfo, control_view_ImageInfo)
# admin.site.register(UserInfo)
