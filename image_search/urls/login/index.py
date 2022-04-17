from django.urls import path
from image_search.views.login.manager import *

urlpatterns = [
    path('', login, name='login'),
    path('check/', login_check, name='login_check'),
    path('register/', register, name='register'),
    path('register_check/', register_check, name='register_check'),
    path('getloginbar/', GetLoginBar, name='get_ogin_ar'),
    path('logout/', Logout, name='logout'),
]
