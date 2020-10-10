from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('', views.TaskViewSet)

urlpatterns = [
    path('/', include(router.urls)),
    path('/done/<int:id>/', views.task_Done, name='task_done')
]