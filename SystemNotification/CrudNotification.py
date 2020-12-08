from SystemNotification.forms import NotificationFormObject
from django.http import Http404,HttpResponseRedirect
from django.shortcuts import render
from SystemNotification.models import Notification

def createNotification(request):
    if request.method == "POST":
        form = NotificationFormObject(request.POST, request.FILES) 
        if form.is_valid(): 
            newObject=form.save()
            w=newObject.get_absolute_url()
            return HttpResponseRedirect(w)
        else:
            return render(request, "mainPage.html", {"message":"form not valid"}) 
    context={
        "form":NotificationFormObject(),
        "message":"This is create Notification.",
        }
    return render(request, "SystemNotification/object.html", context) 
    
def updateNotification(request,pk):
    try:
        obj = Notification.objects.get(pk=pk)
    except Notification.DoesNotExist:
        raise Http404("No MyModel matches the given query.")
  
    
    form = NotificationFormObject(instance = obj)

    if request.method == "POST":
        form = NotificationFormObject(instance = obj, data=request.POST) 
        if form.is_valid(): 
            updateObject=form.save() 
            w=updateObject.get_absolute_url()
            return HttpResponseRedirect(w)
        else:
            raise Http404("Form not valid.") 
    context={
        "form":form,
        "message":"This is update Notification.",
    }
    return render(request, "SystemNotification/object.html", context) 