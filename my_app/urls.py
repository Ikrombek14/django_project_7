from  django.urls import  path
from .views import *

urlpatterns = [
    path('', get_madel, name='madel_list')
]