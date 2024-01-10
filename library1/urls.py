from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

order_router = DefaultRouter()
order_router.register('order', viewset=OrderbookView, basename='order')
order_router.register('return', viewset=ReturningbookView, basename='return book')
urlpatterns = [] + order_router.urls