from django.urls import path
from image_search.views.recommend_user.manager import *

urlpatterns = [
    path('', GetRecommendUser, name='get_recommend_user'),
]
