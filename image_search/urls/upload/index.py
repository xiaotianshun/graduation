from django.urls import path
from image_search.views.upload.manager import Upload, UploadHandle, UploadView, GetView

urlpatterns = [
    path('', Upload, name='upload'),
    path('upload_view/', UploadView, name='upload_view'),
    path('handle/', UploadHandle, name='upload_handle'),
    path('get_view/', GetView, name='get_view'),
]
