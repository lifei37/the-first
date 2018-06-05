"""
创建时间 : 2018/06/03
版本号 : V1
文档名 : auth.py
编辑人 : he_wm
作 用 : 验证用户登录组件
源存储位置 : TmSccity_models\api\views\auth\auth.py
修改及增加功能记录 :
    修改时间 : 
        1、2018/04/02:
        2、
    增加功能时间 :
        1、
        2、   
"""
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from api.models import *


class TmAuth(BaseAuthentication):
    def authenticate(self, request):
        token = request.query_params.get('token')
        obj = UserAuthToken.objects.filter(token=token).first()
        if not obj:
            return AuthenticationFailed({'code': 1001, 'erroe': '认证失败'})
        return (obj.user.username, obj)

