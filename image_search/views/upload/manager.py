from django.http import HttpResponse
from django.shortcuts import render
from image_search.models.userinfo.dao import UserInfo
from image_search.models.imageinfo.dao import ImageInfo


def Upload(request):
    imageinfo = []
    if request.user.is_authenticated:
        imageinfo = list(ImageInfo.objects.filter(
            username=request.user).order_by("-createtime"))
    imageinfo_len = len(imageinfo)
    imageinfo = imageinfo[0:20]

    likeinfo = []
    if request.user.is_authenticated:
        likeinfo = list(ImageInfo.objects.filter(
            username=request.user).order_by("-like_number"))
    likeinfo_len = len(likeinfo)

    likeinfo = likeinfo[0:20]
    return render(request, 'image_search/upload/upload.html', {'imageinfo': imageinfo,
                                                               'imageinfo_len': imageinfo_len,
                                                               'likeinfo': likeinfo,
                                                               'likeinfo_len': likeinfo_len,
                                                               })
