from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin,RetrieveModelMixin, UpdateModelMixin

from drf_day12.models import User
from drf_day12.ser import UserSerializer, UserReadOnlySerializer, UserUpdateSerializer

class RegisterView(GenericViewSet, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        print(self.action)

        if self.action == 'create':
            return UserSerializer
        elif self.action == 'retrieve':
            return UserReadOnlySerializer
        elif self.action == 'update':
            return UserUpdateSerializer
