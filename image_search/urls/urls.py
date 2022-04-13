from django.urls import path
from graduation.image_search.views import views

urlpatterns = [
    path('', views.index, name='index'),
]
