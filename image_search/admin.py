from curses.ascii import US
from django.contrib import admin
from image_search.models.userinfo.dao import UserInfo
from image_search.models.imageinfo.dao import ImageInfo
from image_search.models.imageinfo.fingerprintdao import ImageFP


class control_view_UserInfo(admin.ModelAdmin):
    '''自定义：显示样式'''
    list_display = ['id', 'user', 'nikename', 'createtime', 'head_image']


class control_view_ImageInfo(admin.ModelAdmin):
    list_per_page = 1000
    actions_on_bottom = True  # 【6】底部显示删除动作选项
    actions_on_top = False  # 【7】删除头部动作选项
    list_filter = ['username']  # 【8】列表页右侧过滤栏
    search_fields = ['imagename']  # 【9】列表页上方的搜索框
    '''自定义：显示样式'''
    list_display = ['id', 'username', 'nikename', 'imagename',
                    'createtime', 'image', 'like_number', 'store_number']


class control_view_ImageFP(admin.ModelAdmin):
    list_per_page = 50
    actions_on_bottom = True  # 【6】底部显示删除动作选项
    actions_on_top = False  # 【7】删除头部动作选项
    '''自定义：显示样式'''
    list_display = ['id', 'image',
                    'ahash', 'dhash', 'phash', 'whash']


# Register your models here.
admin.site.register(UserInfo, control_view_UserInfo)
admin.site.register(ImageInfo, control_view_ImageInfo)
admin.site.register(ImageFP, control_view_ImageFP)
# admin.site.register(UserInfo)
admin.site.site_title = "以图搜图后台管理"
admin.site.site_header = "以图搜图后台"
