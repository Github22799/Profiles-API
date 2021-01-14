from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

HelloRouter = DefaultRouter()
HelloRouter.register('HelloViewSet', views.HelloViewSet, basename='HelloViewSet')

urlpatterns = [
    path('HelloAPIView/', views.HelloAPIView.as_view()),
    path('', include(HelloRouter.urls)),
]