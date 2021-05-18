from django.shortcuts import render
from django.urls import path
from . import views

app_name = "website"

urlpatterns = [
    path('base', views.base_page_view, name='base'),
    path('', views.home_page_view, name='home'),
    path('template_1', views.template_1_page_view, name='template_1'),
    path('template_2', views.template_2_page_view, name='template_2')
]
