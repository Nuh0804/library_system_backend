from rest_framework import serializers
from .models import User
from djoser.serializers import UserCreateSerializer, UserSerializer


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
      model = User
      fields = [
         'id',
         'first_name',
         'last_name',
         'username',
         'email',
         'phone_num'
      ]

class UserCreaterSerializer(UserCreateSerializer):
   class Meta(UserCreateSerializer.Meta):
      fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name', 'phone_number']

class CurrentUserSerializer(UserSerializer):
   class Meta(UserSerializer.Meta):
      fields = ['email', 'id', 'username','first_name', 'last_name']
      