from django.urls import path
from image_search.views.upload.manager import Upload

urlpatterns = [
    path('', Upload, name='upload'),
]
