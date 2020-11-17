import json
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
import requests
from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet
from clsp.serializers import *
from clsp.models import *
from django.forms.models import model_to_dict
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
                if(i["nodeId"]== "okapi01"):
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
        response = requests.get(self.url).text
        total_page = int(len(json.loads(response)) / 10) +1
        res = json.loads(response)[(int(p) - 1) * 10:int(p) * 10 ]
        data = {
            "modules": res,
            "total_page": total_page,
            "current_page": p
        }
        return render(request, 'clsp/tenant_list.html', context=data)


class NodeInfoViewSet(ModelViewSet):

    queryset = Nodes.objects.all()
    serializer_class = NodeInfoSerializer

from django.core import serializers
class node_list(View):

    def get(self, request):
        li = []
        nodes = Nodes.objects.all()

        # res_dict = json.loads(serializers.serialize('json',nodes))
        for i in nodes:
            li.append(model_to_dict(i))
        count = len(li)
        p = request.GET.get("p")
        if p == None:
            p = 1
        # total_page = int(int(count) / 10 + 1)
        # total_page = int(count)%10 == 0?int(count)//3:int(count) //3 +1;
        if(int(count)%10 == 0):
            total_page = int(count)//10
        else:
            total_page = int(count) // 10 + 1
        res = li[(int(p) - 1) * 10:int(p) * 10]
        data = {
            "res": res,
            "total_page": total_page,
            "current_page": p
        }
        print(data)
        return render(request, 'clsp/nodes_list.html', data)



def news_type(request):

    return render(request, 'clsp/news_type.html')


def news_edit(request):

    return render(request, 'clsp/news_edit.html')

#节点管理/节点更新
class NodesUpdate(View):
    def post(self, request):
        byte_str = request.body.decode()
        req_data = json.loads(byte_str)
        print(req_data)
        sHandler = req_data.get("sHandler")

        if(sHandler == "delete"):
            id = req_data.get("id")
            node = Nodes.objects.get(id=int(id))
            node.delete()
        elif(sHandler == "edit" ):
            describe = req_data.get("describe").strip()
            ip = req_data.get("ip")
            hostname = req_data.get("hostname")
            id = req_data.get("id")
            try:
                res = Nodes.objects.filter(id=id).update(host_name=hostname,ip=ip,describe=describe)
                logger.info("更新了"+res+"个模块")
            except Exception as e:
                logger.error(e)
        elif(sHandler == "insert"):
            ip = req_data.get("ip")
            hostname = req_data.get("hostname")
            id = req_data.get("id")
            describe = req_data.get("describe").strip()
            Nodes.objects.create(
                ip=ip,
                host_name=hostname,
                describe=describe
            )

        response = {
            "status":"ok"
        }
        return JsonResponse(json.dumps(response), safe=False)



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

