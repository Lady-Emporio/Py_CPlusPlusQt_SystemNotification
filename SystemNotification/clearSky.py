from django.shortcuts import render
import datetime


def usualRender(request,template_name,context=None,content_type=None,status=None,using=None):
    MyContext={
        "data":context,
        "now":datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    return render(request,template_name,MyContext,content_type,status,using)