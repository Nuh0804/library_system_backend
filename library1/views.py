from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import *
# Create your views here.

class OrderbookView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        order = Order.objects.filter(user_id = user.id)
        return order
    def get_serializer_class(self):
        return OrderbookSerializer
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    def perform_create(self, serializer):
        print(self.request.user)
        serializer.save(user= self.request.user)
        return Response(serializer.data)
    

class ReturningbookView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ReturnedBookSerializer
    def get_queryset(self):
        user = self.request.user
        order = Returned.objects.filter(user_id = user.id)
        return order    
    
    def get_serializer(self, *args, **kwargs):
        # Customize the queryset for the 'order' field based on the current user
        user = self.request.user

        kwargs['context'] = self.get_serializer_context()
        kwargs['order_queryset'] = Order.objects.filter(user_id=user)
        return self.serializer_class(*args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user= self.request.user)
        return Response(serializer.data)