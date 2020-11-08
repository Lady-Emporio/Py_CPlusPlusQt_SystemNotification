


from django.urls import include, path
from .views import *
app_name = 'SystemNotification'
urlpatterns = [
    path('all/', index,  {'IsFilter': 'all'},name="AllNotification"),
    path('a/', api_active, name="api_active"),
    path('c/', api_create, name="api_create"),
    path('u/<int:pk>/', api_update, name="api_update"),
    path('', index,  {'IsFilter': 'today'},name="ThisMonthNotification"),
]