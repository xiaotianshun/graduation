from curses.ascii import US
from django.contrib import admin
from graduation.image_search.models.userinfo.dao import UserInfo

# Register your models here.
admin.site.register(UserInfo)
