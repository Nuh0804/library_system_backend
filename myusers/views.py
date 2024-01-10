from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet,generics
from .models import User
from . serializers import RegisterUserSerializer
from rest_framework import status



# Create your views here.
class RegisterUserGet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer

class RegisterUserPost(APIView):
    def post(self, request):
         #queryset = User.objects.get()
         serializer = RegisterUserSerializer(data= request.data)
         if serializer.is_valid():
            serializer.save()
            message = {'save': True}
            return Response(message)
         return Response(status, status= status.HTTP_400_BAD_REQUEST)
    # def post(self, request):
    #     data = request.data
    #     print(request.data)
    #     serializer = RegisterUserSerializer(data=data)
    #     if serializer.is_valid():
    #         email = data['email']
    #         user = User.objects.filter(email=email)
    #         if user:
    #             message = {'status': False, 'message': 'Username already exists'}
    #             return Response(message, status=status.HTTP_400_BAD_REQUEST)
    #         serializer.save()

    #         message = {'save': True}
    #         return Response(message)

    #     message = {'save': False, 'errors': serializer.errors}
    #     return Response(message)

    