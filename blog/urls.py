from django.urls import path
from . import views
#Djangoの path 関数と、blog アプリの全ての ビューをインポートするという意味

urlpatterns=[
    path('', views.post_list, name='post_list'),
]