from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated

from app02.utils import MyJwtAuthentication


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