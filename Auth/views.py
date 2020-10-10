from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.viewsets import mixins
from django.contrib.auth import models as Usermodel  # pylint: disable=W0611
from django.contrib.auth.hashers import make_password
from .serializers import UserModelSerializer
from rest_framework.permissions import IsAdminUser
# Create your views here.


class  UserViewSet(GenericViewSet, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin):

    def perform_create(self, serializer):
        serializer.save(password = make_password(password=self.request.POST.get('password')))

    serializer_class = UserModelSerializer
    queryset = Usermodel.User.objects.all()
    permission_classes = [IsAdminUser]



