"""
创建时间 : 2018/06/04
版本号 : V1
文档名 : newspapers
编辑人 : he_wm
作 用 : 新闻板块接口
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
from api.views.auth.auth import TmAuth


class NewsPapers(ViewSetMixin, APIView):
    authentication_classes = [TmAuth, ]

    def list(self, request, *args, **kwargs):
        """
        新闻主页显示
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret = {'code': 1000, 'data': None}
        try:
            queryset = Article.objects.all()
            ser = ArticleViewSetSerializers(instance=queryset, many=True)
            ret['data'] = ser.data
        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '未获取到资源'
        return Response(ret)

    def retrieve(self, request, *args, **kwargs):
        ret = {'code': 1000, 'data': None}
        try:
            pk = kwargs.get('pk')
            obj = Article.objects.filter(pk=pk).first()
            ser = ArticleDetailViewSetSerializers(instance=obj, many=False)
            ret['data'] = ser.data
        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '未获取到资源'
        return Response(ret)


class AgreeView(ViewSetMixin, APIView):

    def post(self, request, *args, **kwargs):
        """
        点赞
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret = {'code': 1000, 'data': None}
        try:
            pk = kwargs.get('pk')
            # 方式一：更新赞数
            obj = Article.objects.filter(id=pk).first()
            obj.agree_num = obj.agree_num + 1
            obj.save()
            # 方式二：更新赞数
            # F，更新数据库字段
            # Q, 构造复杂条件
            # from django.db.models import F,Q
            # v = Article.objects.filter(id=pk).update(agree_num=F("agree_num") + 1)
            # print(v)
            ret['data'] = obj.agree_num
        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '点赞失败'
        return Response(ret)
