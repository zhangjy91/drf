from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from drf_day12.models import User

class UserSerializer(ModelSerializer):
    re_password = serializers.CharField(max_length=16, min_length=4, required=True, write_only=True)
    class Meta:
        model = User
        fields = ['username','password', 'mobile','re_password','icon']

        extra_kwargs = {
            'username':{'max_length':16},
        }

    #局部钩子
    def validate_mobile(self, data):
        if len(data) != 11:
            raise ValidationError('手机号不合法')
        return data

    #全局钩子
    def validate(self, attrs):
        if attrs.get('password') == attrs.get('re_password'):
            attrs.pop('re_password') #删除该字段，因为数据库里没有该字段
            return attrs
        else:
            raise ValidationError('密码不一致')

    #密码是加密显示的
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UserReadOnlySerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'icon']


class UserUpdateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['icon']
