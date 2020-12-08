
from django.forms import ModelForm
from .models import Notification,GroupNotification

from django import forms
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string
class ButtonWidget(forms.Widget):

    def render(self,name, value, attrs=None, renderer=None):
        sv=value.strftime("%Y-%m-%dT%H:%M:%S")
        return f"<input type='datetime-local' name='{name}' class='ObjectPeriod'  value='{sv}' step='1'>"

class NotificationFormObject(ModelForm):
    class Meta:
        model = Notification
        fields = '__all__'
        widgets = {
            "period":ButtonWidget,
        }

class GroupNotificationFormObject(ModelForm):
    class Meta:
        model = GroupNotification
        fields = '__all__'


from django import forms

class NotificationFormUpdate(forms.Form):
    StateId = forms.IntegerField()

class NotificationFormCreate(forms.Form):
    GroupName = forms.CharField(max_length=150,required=False)
    NotName = forms.CharField(max_length=150)



