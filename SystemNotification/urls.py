# -*- coding: utf-8 -*-


#from django.urls import include, path
from django.conf.urls import url
from .views import *
from django.urls import path, re_path
import SystemNotification.CrudNotification as CrudNotification

app_name = 'SystemNotification'
urlpatterns = [
    re_path(r'^all/', index,  {'IsFilter': 'all'},name="AllNotification"),
    re_path(r'^month/', index,  {'IsFilter': 'today'},name="ThisMonthNotification"),
    re_path(r'^a/', api_active, name="api_active"),
    re_path(r'^c/', api_create, name="api_create"),
    re_path(r'^u/<int:pk>/', api_update, name="api_update"),

    re_path(r'^n/c/',      CrudNotification.createNotification, name='createObjectNotification'), 
    re_path(r'^n/(?P<pk>\d+)/', CrudNotification.updateNotification, name="updateObjectNotification"),
    re_path(r'^test_pk/(?P<pk>\d+)/', view_test_pk, name="test_pk"),
    re_path(r'^test_pk_create/', test_pk_create, name="test_pk_create"),
    re_path(r'^test_page_choose/', test_page_choose, name="test_page_choose"),
    re_path(r'^test_page_list/', Notification_list_paginator, name="Notification_list_paginator"),
    
    re_path(r'^$', index,  {'IsFilter': 'active'},name="activeNotification"),


    re_path(r'^ajax/comment/$', api_SaveComment,name="apiSaveComment"),
]



from django.conf.urls import handler404


handler404 = 'M404.html'
def handler404(request, *args, **argv):
    response = render_to_response('M404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response