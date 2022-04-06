from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated

from app02.utils import MyJwtAuthentication
from app02.ser import LoginSerializer

class OrderView(APIView):
    authentication_classes = [JSONWebTokenAuthentication,]
    permission_classes = [IsAuthenticated,]
    def get(self,request):
        return Response({'msg':'这是订单信息'})

class GoodView(APIView):
    authentication_classes = [MyJwtAuthentication,]

    def get(self,request,*args,**kwargs):
        print(request.user)
        return Response({'msg':'这是商品信息'})


class Login2View(ViewSet):

    def login(self,request,*args,**kwargs):
        login_ser = LoginSerializer(data=request.data, context={'request':request})
        login_ser.is_valid(raise_exception=True)
        token = login_ser.context.get('token')
        username = login_ser.context.get('username')
        return Response({'status':100, 'msg':'登录成功', 'token':token, 'username':username})
