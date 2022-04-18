from django.http import HttpResponse
from django.shortcuts import render
from image_search.models.userinfo.dao import UserInfo
from image_search.models.imageinfo.dao import ImageInfo
import random


def Share(request):
    imageInfo = ImageInfo.objects.all()
    imageInfo = list(imageInfo)
    imageInfo = random.sample(imageInfo, min(len(imageInfo), 10))
    imageinfo_len = len(imageInfo)
    return render(request, 'image_search/share/share.html', {'imageinfo': imageInfo,
                                                             'imageinfo_len': imageinfo_len,
                                                             })
