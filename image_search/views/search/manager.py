from ctypes import resize
from email.mime import image
import os
import time
from unittest import result
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from graduation.settings import MEDIA_ROOT
from image_search.models.userinfo.dao import UserInfo
from image_search.models.imageinfo.dao import ImageInfo
from image_search.models.imageinfo.fingerprintdao import ImageFP
from django.views.decorators.csrf import csrf_exempt, csrf_protect  # Add this
import imagehash
from PIL import Image


def Search(request):
    if request.method == 'GET':
        return render(request, 'image_search/search/search.html')
    elif request.method == 'POST' and request.FILES.get('pic', None) != None:
        recallinfo = Recall(request)
        return render(request, 'image_search/search/search.html', recallinfo)
    return render(request, 'image_search/search/search.html')


def diff(ori_hash, oth_hash):
    return ori_hash - imagehash.hex_to_hash(oth_hash)


def Recall(request):
    dataset = list(ImageFP.objects.all())
    pic = request.FILES['pic']
    ori_name = pic.name
    save_path = "%s/search_src/%s" % (MEDIA_ROOT, ori_name)

    with open(save_path, 'wb') as f:
        for content in pic.chunks():
            f.write(content)

    phash = imagehash.phash(Image.open(pic), 12)
    result = [(item, (1 - diff(phash, item.phash)/64)*100., diff(phash, item.phash))
              for item in dataset if diff(phash, item.phash) < 30]

    result.sort(key=lambda x: x[1], reverse=True)
    print("/media/search_src/%s" % (ori_name))
    print('result:', result)
    return {
        'src_image': "/media/search_src/%s" % (ori_name),
        'ori_name': ori_name,
        'result': result,
    }
