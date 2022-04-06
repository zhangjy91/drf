from drf_day12.models import User

from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework_jwt.utils import jwt_decode_handler,jwt_payload_handler,jwt_encode_handler
import re

class LoginSerializer(ModelSerializer):
    username = serializers.CharField() #数据库中username是unique的，走的是post请求，系统认为是保存数据，
                                        # 但数据库中已存在此数据，此时自身校验就没通过，也就不会再走下面的valiadate校验
    class Meta:
        model = User
        fields = ['username', 'password']

    def validate(self, attrs):

        print(self.context)

        username = attrs.get('username')
        password = attrs.get('password')

        if re.match('^1[3-9][0-9]{9}',username):
            user = User.objects.filter(mobile=username).first()
        elif re.match('^.+@.+$',username):
            user = User.objects.filter(email=username).first()
        else:
            user = User.objects.filter(username=username).first()

        if user:
            if user.check_password(password):
                payload = jwt_payload_handler(user)
                token= jwt_encode_handler(payload)
                self.context['token'] = token
                self.context['username'] = user.username
                return attrs
            else:
                raise ValidationError('密码错误')
        else:
            raise ValidationError('用户不存在')