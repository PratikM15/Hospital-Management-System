from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('add', views.add, name="add"),
    path('update', views.update, name="update"),
    path('delete', views.delete, name="delete"),
    path('modify', views.modify, name="modify"),
    path('search', views.search, name="search"),
]