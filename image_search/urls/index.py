from django.urls import path, include
from image_search.views.manager import index

urlpatterns = [
    path("", index, name="index"),
    path("login/", include("image_search.urls.login.index")),
    path("upload/", include("image_search.urls.upload.index")),
    path("share/", include("image_search.urls.share.index")),
    path("search/", include("image_search.urls.search.index")),
    path("recommend_user/", include("image_search.urls.recommend_user.index"),
         name="recommend_user"),
]
