from django import template
import datetime 
from django.contrib.admin.models import LogEntry
register = template.Library()
 
@register.inclusion_tag('tags/MyTagHeader.html')
def MyTagHeader():
    return {
        "now":datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }




@register.inclusion_tag('tags/MyTagLastAction.html')
def MyTagLastAction():
    lastLog=list(LogEntry.objects.order_by('-action_time')[:10]) #lastLog[0]
    #action_time datetime
    #object_repr	'<Задача: 1: we are from None -None>'	str
    #choices=[(1, 'Addition'), (2, 'Change'), (3, 'Deletion')],
    w=[]
    for i in lastLog:
        d={
            "action_time":i.action_time.strftime("%Y-%m-%d %H:%M:%S"),
            "is_addition":i.is_addition(),
            "is_change":i.is_change(),
            "is_deletion":i.is_deletion(),
            "get_action_flag_display":i.get_action_flag_display(),
            "get_admin_url":i.get_admin_url(),
            "get_change_message":i.get_change_message(),
            "pk":i.pk,
            "object_repr":i.object_repr,
            "user":i.user,
            }
        w.append(d)
    return {
        "lastLog":w,
        }