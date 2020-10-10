from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.viewsets import mixins
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from datetime import datetime
from .serializers import TaskSerializer
from . import models

# Create your views here.


class TaskViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, GenericViewSet, mixins.ListModelMixin):

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


    def perform_update(self,serializer):
        task = get_object_or_404(models.Task,pk=self.request.POST.get('id'))
        if task.user == self.request.user:
            serializer.save()
        else:
            print('no such a task')
            raise NotFound("No such Task", code=status.HTTP_404_NOT_FOUND)


    def get_queryset(self):
        return models.Task.objects.filter(user=self.request.user).order_by('created_date')


    
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    queryset = models.Task.objects.all()




@api_view()
def task_Done(request, id):
    task = get_object_or_404(models.Task, pk=id)
    if task.user == request.user:
        print(task.is_done)
        task.is_done = not task.is_done
        task.finished_date = datetime.now()
        task.save()
        return Response({'task_status': task.is_done, 'last_update': task.finished_date}, status=status.HTTP_200_OK)
    else:
        return Response({'task_status': 'no such a task'}, status=status.HTTP_404_NOT_FOUND)
    return Response({'task_status': 'missing arguments'}, status=status.HTTP_400_BAD_REQUEST)
