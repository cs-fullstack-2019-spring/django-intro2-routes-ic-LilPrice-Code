from django.urls import path

from . import views

urlpatterns = [
    path('mycity/', views.mycity, name='city'),
    path('myeats/', views.myeats, name='index'),
]
