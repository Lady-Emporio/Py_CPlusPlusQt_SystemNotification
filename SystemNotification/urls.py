# -*- coding: utf-8 -*-


#from django.urls import include, path
from django.conf.urls import url
from .views import *
app_name = 'SystemNotification'
urlpatterns = [
    url('all/', index,  {'IsFilter': 'all'},name="AllNotification"),
    url('month/', index,  {'IsFilter': 'today'},name="ThisMonthNotification"),
    url('a/', api_active, name="api_active"),
    url('c/', api_create, name="api_create"),
    url('u/<int:pk>/', api_update, name="api_update"),
    url('', index,  {'IsFilter': 'active'},name="activeNotification"),
]