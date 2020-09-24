from django.urls import path
from .views import *


urlpatterns = [
    path('', my_view, name='my-view'),
    path('index/', index, name='index'),
    path('main/', main, name='main_'),
    path('', download)
]
