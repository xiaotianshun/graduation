from django.urls import path
from image_search.views.login.manager import index

urlpatterns = [
    path('', index, name='index'),
]
