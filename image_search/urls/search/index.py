from django.urls import path
from image_search.views.search.manager import Search

urlpatterns = [
    path('', Search, name='search'),
]
