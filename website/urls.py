from django.contrib import admin
from django.urls import path
from . import views,models

urlpatterns = [
    path('',views.home,name='home'),
    path('blogs', views.blogs,name='blogs'),
    path('blog/<str:slug>',views.blog,name='blog'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('news',views.news,name='news'),
    path('Cryptoprice',views.cryptoprice,name='cryptoprice'),
]
