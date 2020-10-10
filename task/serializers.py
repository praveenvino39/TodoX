from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import  Task
from Auth.serializers import UserModelSerializer


class TaskSerializer(ModelSerializer):
    class Meta():
        model = Task
        fields = ['user','id', 'title', 'is_done', 'finished_date',]
