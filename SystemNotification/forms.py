
from django.forms import ModelForm
from .models import Notification

#class NotificationForm(ModelForm):
#    class Meta:
#        model = Notification
#        fields = ['name', 'state']


from django import forms

class NotificationFormUpdate(forms.Form):
    StateId = forms.IntegerField()

class NotificationFormCreate(forms.Form):
    GroupName = forms.CharField(max_length=150,required=False)
    NotName = forms.CharField(max_length=150)