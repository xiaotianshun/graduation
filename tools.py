import os
from image_search.views.upload.manager import ImageFPCreat
from django.contrib.auth.models import User
from image_search.models.imageinfo.dao import ImageInfo


def AddImage():
    user = User.objects.get(id=7)
    print(user)
    path = "/home/yoloxiao/project/graduation/data"
    datanames = os.listdir(path)
    for name in datanames:
        print(name)
        src_path = "/home/yoloxiao/project/graduation/data/" + name
        dist_path = "/home/yoloxiao/project/graduation/media/image/" + name
        os.system("cp %s %s" % (src_path, dist_path))
        webname = "image/" + name
        obj = {
            'username': user,
            'imagename': '数据集_' + name.split('.')[0],
            'image': webname,
        }
        imageinfo = ImageInfo.objects.create(**obj)
        save_path = src_path
        ImageFPCreat('', imageinfo, save_path)


AddImage()
