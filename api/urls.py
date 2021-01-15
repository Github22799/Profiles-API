from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('HelloViewSet', views.HelloViewSet, basename='HelloViewSet')
router.register('profile', views.UserProfileViewSet)
router.register('status', views.UserStatusViewSet)


urlpatterns = [
    path('HelloAPIView/', views.HelloAPIView.as_view()),
    path('login/', views.UserLoginAPIView.as_view()),
    path('', include(router.urls)),
]