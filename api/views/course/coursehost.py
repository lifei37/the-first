"""
创建时间 : 2018/05/31
版本号 : V1
文档名 : coursehost.py
编辑人 : he_wm
作 用 : 为课程分栏提供数据
源存储位置 : TmSccity_models\api\views\course\coursehost.py
修改及增加功能记录 :
    修改时间 :
        1、2018/04/02:
        2、
    增加功能时间 :
        1、
        2、
"""
from api.models import *
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ViewSetMixin
from api.serializers.coursehost import *


# Create your views here.

class CourseViewSet(ViewSetMixin, APIView):
    def list(self, request, *args, **kwargs):
        """
        课程主页显示资源
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret = {'code': 1000, 'data': None}
        try:
            queryset = Course.objects.all()
            ser =CourseViewSetSerializers(instance=queryset, many=True)
            ret['data'] = ser.data
        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '未获取到资源'
        return Response(ret)

    def retrieve(self, request, *args, **kwargs):
        ret = {'code': 1000, 'data': None}
        try:
            pk = kwargs.get('pk')
            obj = CourseDetail.objects.filter(id=pk).first()
            ser = CourseDetailViewSetSerializers(instance=obj, many=False)
            ret['data'] = ser.data
        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '未获取到资源'
        return Response(ret)
