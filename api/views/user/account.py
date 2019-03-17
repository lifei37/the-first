# -*- coding: utf-8 -*-
"""
创建时间 : 2018/06/03
版本号 : V1
文档名 : account.py
编辑人 : he_wm
作 用 : 用户登录控制
源存储位置 : TmSccity_models\\api\\views\\user\\account.py
修改及增加功能记录 :
    修改时间 :
        1、2018/04/02:
        2、
    增加功能时间 :
"""
import uuid

from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist

from api.models import *
from utils.response import BaseResponse


class loginView(APIView):
    """
    用于用户认证相关接口
    """

    def post(self, request, *args, **kwargs):
        """
        用户认证
        :param request: 请求相关的数据
        :param args: URL传参
        :param kwargs: URL关键字传参
        :return:
        """
        ret = BaseResponse()
        try:
            user = request.data.get('user')
            pwd = request.data.get('pwd')
            user = Account.objects.filter(username=user, password=pwd).first()
            if not user:
                ret.code = 1001
                ret.error = '用户名或密码错误'
                return Response(ret)

            uid = str(uuid.uuid4())
            UserAuthToken.objects.update_or_create(user=user, defaults={'token': uid})
            ret.data = uid
        except Exception as e:
            ret.code = 1003

        return Response(ret.dict)
