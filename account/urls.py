from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('signup/', views.signUp, name='signup'),
    path('signin/', views.signin, name='sigin')

]