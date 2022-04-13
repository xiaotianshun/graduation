from django.http import HttpResponse
from django.shortcuts import render
from image_search.models.userinfo.dao import UserInfo


def GetRecommendUser(request):
    userinfo = UserInfo.objects.all()
    return render(request, 'image_search/recommend_user/GetRecommendUser.html', {'userinfo': userinfo})
