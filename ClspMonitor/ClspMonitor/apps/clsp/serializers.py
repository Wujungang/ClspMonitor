from rest_framework import serializers

from clsp.models import *
from rest_framework.serializers import Serializer,ModelSerializer


class NodeInfoSerializer(Serializer):
    id = serializers.IntegerField(label='ID', read_only=True,required=False)
    ip = serializers.CharField(label="ip地址",max_length=255,required=True)
    host_name = serializers.CharField(label="主机名称",max_length=255,required=False)
    node_name = serializers.CharField(label="节点名称",max_length=255,required=False)
    pass_word = serializers.CharField(label="密码",max_length=255,required=False)
    pri_key = serializers.CharField(label="私钥信息",required=False)
    module = serializers.StringRelatedField(label='模块',required=False)
    class Meta:
        model = Nodes
        fields = '__all__'


class ModulesInfoSerializer(ModelSerializer):
    class Meta:
        model = Modules
        fields = '__all__'

