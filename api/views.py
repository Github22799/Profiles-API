from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import HelloSerializer


class HelloAPIView(APIView):

    serializer_class = HelloSerializer

    def get(self, request, format=None):
        message = 'Hello there!'
        elements = ['a', 'b', 'c']

        return Response({'message': message, 'elements': elements})

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data['name']
            message = f'Hello {name}!'
            return Response({'message': message})
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):

    serializer_class = HelloSerializer

    def list(self, request):
        serializer_class = HelloSerializer

        message = 'Hello there!'
        elements = ['a', 'b', 'c']

        return Response({'message': message, 'elements': elements})

    def retrieve(self, request, pk=None):
        return Response({'method': 'GET'})

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data['name']
            message = f'Hello {name}!'
            return Response({'message': message})
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        return Response({'method': 'PUT'})

    def partial_update(self, request, pk=None):
        return Response({'method': 'PATCH'})

    def destroy(self, request, pk=None):
        return Response({'method': 'DELETE'})


