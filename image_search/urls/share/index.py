from django.urls import path
from image_search.views.share.manager import Share

urlpatterns = [
    path('', Share, name='share'),
]
