from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from Auth.views import UserViewSet

router = DefaultRouter()
router.register('/user', UserViewSet, basename='listUsers')

urlpatterns = [
    path('', include(router.urls)),
    path('/login/', obtain_auth_token)
]