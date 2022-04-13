from django.urls import path, include

urlpatterns = [
    path("login/", include("image_search.urls.login.index")),
    path("recommend_user/", include("image_search.urls.recommend_user.index")),
]
