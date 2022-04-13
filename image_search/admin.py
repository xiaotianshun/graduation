from curses.ascii import US
from django.contrib import admin
from image_search.models.userinfo.dao import UserInfo


class control_view_UserInfo(admin.ModelAdmin):
    '''自定义：显示样式'''
    list_display = ['id', 'user', 'nikename', 'createtime', 'head_image']


# Register your models here.
admin.site.register(UserInfo, control_view_UserInfo)
# admin.site.register(UserInfo)
