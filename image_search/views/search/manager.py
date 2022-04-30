from cgi import print_arguments
from ctypes import resize
from email.mime import image
import os
import random
import time
from unittest import result
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from graduation.settings import MEDIA_ROOT
from image_search.models.userinfo.dao import UserInfo
from image_search.views.tools.yolov5 import GetImageTag
from image_search.views.tools.faiss import faiss_search
from image_search.models.imageinfo.dao import ImageInfo
from image_search.models.imagetag.dao import ImageTag, THRESHOLD
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


def FuzzySearch(request):
    if request.method == 'GET':
        return render(request, 'image_search/fuzzy_search/fuzzy_search.html')
    elif request.method == 'POST' and request.FILES.get('pic', None) != None:
        recallinfo = TagRecall(request)
        return render(request, 'image_search/fuzzy_search/fuzzy_search.html', recallinfo)
    return render(request, 'image_search/fuzzy_search/fuzzy_search.html')


def diff(ori_hash, oth_hash):
    return ori_hash - imagehash.hex_to_hash(oth_hash)


def Recall(request):
    pic = request.FILES['pic']
    ori_name = pic.name
    save_path = "%s/search_src/%s" % (MEDIA_ROOT, ori_name)

    with open(save_path, 'wb') as f:
        for content in pic.chunks():
            f.write(content)

    phash = imagehash.phash(Image.open(pic), 12)
    index, dis = faiss_search(str(phash), 30)
    dataset = ImageFP.objects.filter(id__in=index)
    print(index, dis)
    print(dataset)
    result = [(item, (1 - diff(phash, item.phash)/64)*100., diff(phash, item.phash))
              for item in dataset]
    result.sort(key=lambda x: x[1], reverse=True)
    print('result:', result)
    return {
        'src_image': "/media/search_src/%s" % (ori_name),
        'ori_name': ori_name,
        'result': result,
    }


def TagRecall(request):
    dataset = list(ImageFP.objects.all())
    pic = request.FILES['pic']
    ori_name = pic.name
    save_path = "%s/search_src/%s" % (MEDIA_ROOT, ori_name)
    dist_save_dir = "%s/search_src/tag" % (MEDIA_ROOT)

    with open(save_path, 'wb') as f:
        for content in pic.chunks():
            f.write(content)

    tag = GetImageTag(save_path, dist_save_dir)
    tags = [key for key, val in tag.items() if val > THRESHOLD]
    imagetag = ImageTag.objects.filter(tag__in=tags, score__gt=THRESHOLD)
    print(tags)
    result = [item.imageinfo for item in imagetag]
    print('recall size =', len(result))
    result = random.sample(result, min(len(result), 20))
    print(result)
    # phash = imagehash.phash(Image.open(pic), 12)
    # result = [(item, (1 - diff(phash, item.phash)/64)*100., diff(phash, item.phash))
    #           for item in dataset if diff(phash, item.phash) < 30]

    # result.sort(key=lambda x: x[1], reverse=True)
    # print("/media/search_src/%s" % (ori_name))
    # print('result:', result)

    return {
        'src_image': "/media/search_src/tag/%s" % (ori_name.split('.')[0] + '.jpg'),
        'ori_name': '未识别' if not tags else ' '.join(tags),
        'result': result,
    }
