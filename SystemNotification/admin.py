from django.contrib import admin	
from .models import *	
	
admin.site.register(NotificationState)	
admin.site.register(GroupNotification)	


class NotificationHistoryAdmin(admin.ModelAdmin):	
	list_display = ("id","notification","period","state")
	list_display_link = ("id")
	search_fields = ("notification","state")


class NotificationHistoryInline(admin.TabularInline):
	model = NotificationHistory
	extra= 0

class NotificationAdmin(admin.ModelAdmin):	
	list_display = ("id","name","parent","period","state","isActive")
	list_display_link = ("id")
	search_fields = ("name","parent__name")
	list_filter = ("name","parent","period","state","isActive")
	save_as =True #replace Save and add another
	inlines = [
        NotificationHistoryInline,
    ]
	save_on_top=True

admin.site.register(NotificationHistory,NotificationHistoryAdmin)	
admin.site.register(Notification,NotificationAdmin)	