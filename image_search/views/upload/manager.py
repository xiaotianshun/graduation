from email.mime import image
import os
import time
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from graduation.settings import MEDIA_ROOT
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


def UploadHandle(request):
    if request.FILES.get('pic', None) == None:
        return HttpResponse('请先选择需上传图片')
    pic = request.FILES['pic']
    imagename = pic.name
    filename = str(request.user.id) + "_" + \
        str(int(time.time())) + os.path.splitext(imagename)[-1]

    save_path = "%s/image/%s" % (MEDIA_ROOT, filename)
    with open(save_path, 'wb') as f:
        for content in pic.chunks():
            f.write(content)

    obj = {
        'username': request.user,
        'imagename': imagename,
        'image': 'image/' + filename,
    }
    ImageInfo.objects.create(**obj)

    return redirect("http://43.154.99.88:8000/upload")


def UploadView(request):
    return render(request, 'image_search/upload/upload_view.html')


def GetView(request):
    action = request.GET.get('action')
    if action == 'get_ori_img':
        return GetOriImg(request)
    return JsonResponse({})


def GetOriImg(request):
    obj = ImageInfo.objects.filter(username=request.user).last()
    return JsonResponse({'path': str(obj.image)})
