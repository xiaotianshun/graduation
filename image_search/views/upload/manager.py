from email.mime import image
import os
import time
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from graduation.settings import MEDIA_ROOT
from image_search.models.userinfo.dao import UserInfo
from image_search.models.imageinfo.dao import ImageInfo
from image_search.models.imageinfo.fingerprintdao import ImageFP
from django.views.decorators.csrf import csrf_exempt, csrf_protect  # Add this
import imagehash
from PIL import Image


def Upload(request):
    imageinfo = []
    if request.user.is_authenticated:
        imageinfo = list(ImageInfo.objects.filter(
            username=request.user).order_by("-createtime"))
    imageinfo_len = len(imageinfo)
    imageinfo = imageinfo[0:10]

    likeinfo = []
    if request.user.is_authenticated:
        likeinfo = list(ImageInfo.objects.filter(
            username=request.user).order_by("-like_number"))
    likeinfo_len = len(likeinfo)

    likeinfo = likeinfo[0:10]
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
    filename = str(int(time.time())) + \
        os.path.splitext(imagename)[-1] + "_" + str(request.user.id)

    save_path = "%s/image/%s" % (MEDIA_ROOT, filename)

    with open(save_path, 'wb') as f:
        for content in pic.chunks():
            f.write(content)

    obj = {
        'username': request.user,
        'imagename': imagename,
        'image': 'image/' + filename,
    }
    imageinfo = ImageInfo.objects.create(**obj)
    ImageFPCreat(request, imageinfo, save_path)
    return redirect("/upload")


def ImageFPCreat(request, imageinfo, save_path):

    ahash = imagehash.average_hash(Image.open(save_path), 12)
    dhash = imagehash.dhash(Image.open(save_path), 12)
    phash = imagehash.phash(Image.open(save_path), 12)
    whash = imagehash.whash(Image.open(save_path), 8)
    print(ahash, dhash, phash, whash)
    ImageFP.objects.create(imageinfo=imageinfo, ahash=ahash,
                           dhash=dhash, phash=phash, whash=whash)
    return 0


def UploadView(request):
    return render(request, 'image_search/upload/upload_view.html')


def GetView(request):
    # 创建临时目录
    obj = ImageInfo.objects.filter(username=request.user).last()
    dirname = str(obj.image).split('/')[-1].split('.')[0]
    path = MEDIA_ROOT + '/temp/' + dirname
    ori_path = MEDIA_ROOT + '/' + str(obj.image)
    folder = os.path.exists(MEDIA_ROOT + '/temp/' + dirname)
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)

    action = request.GET.get('action')
    if action == 'get_ori_img':
        return GetOriImg(request)
    elif action == 'get_gray_img':
        return GetGrayImg(request, ori_path, '/temp/' + dirname + '/gray_' + str(obj.image).split('/')[-1])
    elif action == 'get_fuzzy_img':
        return GetFuzzyImg(request, ori_path, '/temp/' + dirname + '/fuzzy_' + str(obj.image).split('/')[-1])
    elif action == 'get_dct_img':
        return GetDctImg(request, ori_path, '/temp/' + dirname + '/dct_' + str(obj.image).split('/')[-1])
    elif action == 'get_image_fp':
        return GetImageFP(request, obj)
    return JsonResponse({})


def GetOriImg(request):
    obj = ImageInfo.objects.filter(username=request.user).last()
    return JsonResponse({'path': str(obj.image)})


def GetGrayImg(request, oripath, distpath):
    Image.open(oripath).convert("L").save(MEDIA_ROOT + distpath, "JPEG")
    return JsonResponse({'path': distpath})


def GetFuzzyImg(request, oripath, distpath):
    hash_size, highfreq_factor = 12, 4
    img_size = hash_size * highfreq_factor
    Image.open(oripath).convert("L").resize(
        (img_size, img_size), Image.ANTIALIAS).save(MEDIA_ROOT + distpath, "JPEG")
    return JsonResponse({'path': distpath})


def GetDctImg(request, oripath, distpath):
    import numpy
    import scipy.fftpack
    hash_size, highfreq_factor = 12, 4
    img_size = hash_size * highfreq_factor
    image = Image.open(oripath).convert("L").resize(
        (img_size, img_size), Image.ANTIALIAS)
    pixels = numpy.asarray(image)
    dct = scipy.fftpack.dct(scipy.fftpack.dct(pixels, axis=0), axis=1)
    dctlowfreq = dct[:hash_size, :hash_size]

    Image.fromarray(dctlowfreq).convert(
        'L').save(MEDIA_ROOT + distpath, "JPEG")
    return JsonResponse({'path': distpath})


def GetImageFP(request, image):
    obj = ImageFP.objects.get(imageinfo=image)
    return JsonResponse({
        'ahash': obj.ahash,
        'dhash': obj.dhash,
        'phash': obj.phash,
        'whash': obj.whash,
    })
