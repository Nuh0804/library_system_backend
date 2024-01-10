
from django.urls import path
from . import views

urlpatterns = [
    path('register', views.RegisterUserGet.as_view({'get': 'list'}), name= 'registeruser'),
     path('', views.RegisterUserPost.as_view(), name= 'registeruser')
]