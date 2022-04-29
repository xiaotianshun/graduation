from django.http import HttpResponse
from django.shortcuts import render
from matplotlib import use
from numpy import printoptions
from image_search.models.userinfo.dao import UserInfo
from image_search.models.imageinfo.dao import ImageInfo
from image_search.models.imagetag.dao import ImageTag, THRESHOLD, SHARE_THRESHOLD

import random


def Share(request):
    userinfo = UserInfo.objects.get(user=request.user)
    hobby_list = list(filter(None, userinfo.hobby_tag.split(' ')))
    print(hobby_list)

    imagetag = ImageTag.objects.filter(
        tag__in=hobby_list, score__gt=SHARE_THRESHOLD)
    imageInfo = [item.imageinfo for item in imagetag]
    imageInfo = random.sample(imageInfo, min(len(imageInfo), 10))
    imageinfo_len = len(imageInfo)
    for item in imageInfo:
        print(item.all_tag)
    return render(request, 'image_search/share/share.html', {'imageinfo': imageInfo,
                                                             'imageinfo_len': imageinfo_len,
                                                             })
