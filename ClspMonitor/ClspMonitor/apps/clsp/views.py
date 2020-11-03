import json

from django.shortcuts import render
import os
from django.views.generic import View
from django.http import HttpResponse
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
from clsp.models import Modules,Nodes
import requests
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.core import serializers
from rest_framework.views import APIView
import logging
# Create your views here.

logger = logging.getLogger("django")


def index(request):
    return render(request, 'clsp/index.html')


class UserCount(View):
    def __init__(self):
        self.url = 'http://39.106.33.252:9130/_/discovery/modules'
        self.okapi01 = []
        self.okapi02 = []
        self.okapi03 = []

    def get(self, request):
        res = requests.get(self.url).text
        for i in json.loads(res):
            if i.get("nodeId"):
                if(i["nodeId"] == "okapi01"):
                    self.okapi01.append(i["nodeId"])
                elif(i["nodeId"] == "okapi02"):
                    self.okapi02.append(i["nodeId"])
                elif (i["nodeId"] == "okapi03"):
                    self.okapi03.append(i["nodeId"])
            elif i.get("srvcId"):
                if(i["srvcId"].count("okapi01") != -1):
                    self.okapi01.append("okapi01")
                elif(i["srvcId"].count("okapi02") != -1):
                    self.okapi01.append("okapi02")
                elif (i["srvcId"].count("okapi03") != -1):
                    self.okapi01.append("okapi03")

        data = {
            "okapi01":len(self.okapi01),
            "okapi02":len(self.okapi02),
            "okapi03":len(self.okapi03),
        }
        return render(request, 'clsp/user_count.html',context=data)

class user_list(View):

    def __init__(self):
        self.url = 'http://39.106.33.252:9130/_/discovery/modules'
        self.instances = {}
        self.okapi01 = []
        self.okapi02 = []
        self.okapi03 = []

    def get(self, request):
        res = requests.get(self.url).text
        result = json.loads(res)
        for i in result:
            if i.get("nodeId"):
                if (i["nodeId"] == "okapi01"):
                    self.okapi01.append(i["nodeId"])
                elif (i["nodeId"] == "okapi02"):
                    self.okapi02.append(i["nodeId"])
                elif (i["nodeId"] == "okapi03"):
                    self.okapi03.append(i["nodeId"])
            elif i.get("srvcId"):
                if (i["srvcId"].count("okapi01") != -1):
                    self.okapi01.append("okapi01")
                elif (i["srvcId"].count("okapi02") != -1):
                    self.okapi01.append("okapi02")
                elif (i["srvcId"].count("okapi03") != -1):
                    self.okapi01.append("okapi03")
        data = {
            "okapi01": len(self.okapi01),
            "okapi02": len(self.okapi02),
            "okapi03": len(self.okapi03),
            "ins":result
        }
        return render(request, 'clsp/user_list.html', context=data)


class news_review(View):

    def __init__(self):
        self.url = "http://39.106.33.252/okapia/_/proxy/modules"

    def get(self, request):
        response = requests.get(self.url).text

        data = {
            "modules": json.loads(response)
        }
        return render(request, 'clsp/news_review.html',context=data)

class tenant_list(View):

    def __init__(self):
        self.url = "http://39.106.33.252:9130/_/proxy/tenants"

    def get(self, request):
        p = request.GET.get("p")
        if p == None:
            p = 1
        print(p)
        response = requests.get(self.url).text
        total_page = int(len(json.loads(response)) / 10) +1
        print(total_page)
        res = json.loads(response)[(int(p) - 1) * 10:int(p) * 10 ]

        data = {
            "modules": res,
            "total_page": total_page,
            "current_page": p
        }
        return render(request, 'clsp/tenant_list.html', context=data)
def pagation(request):
    url = "http://39.106.33.252:9130/_/proxy/tenants"
    p = request.GET.get("p")
    response = requests.get(url).text
    total_page = json.loads(response)/20
    res = json.loads(response)[(p-1)*10:p*10-1]
    data = {
        "total_page": total_page,
        "current_page": p,
        "users": res
    }
    return JsonResponse(data)




def news_type(request):

    return render(request, 'clsp/news_type.html')


def news_edit(request):

    return render(request, 'clsp/news_edit.html')


def news_review_detail(request):

    return render(request, 'clsp/news_review_detail.html')


class RegisterView(View):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return HttpResponse("我是get")

    def post(self, request):
        return HttpResponse("我是post")


def middleware(request):
    print('view 视图被调用')
    return HttpResponse('OK')

