from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as djangoLogin


def index(request):
    return render(request, "image_search/index.html")
