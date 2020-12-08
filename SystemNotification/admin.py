from django.contrib import admin	
from .models import *	


admin.site.register(NotificationState)

class GroupNotificationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ['id']
    actions = []

admin.site.register(GroupNotification,GroupNotificationAdmin)	



class NotificationHistoryAdmin(admin.ModelAdmin):	
	list_display = ("id","notification","period","state")
	list_display_link = ("id")
	search_fields = ("notification","state")


class NotificationHistoryInline(admin.TabularInline):
	model = NotificationHistory
	extra= 0

class SubNotificationCommentsInline(admin.TabularInline):
	model = SubNotificationComments
	extra= 0

class NotificationAdmin(admin.ModelAdmin):	
	list_display = ("id","name","parent","period","state","isActive")
	list_display_link = ("id")
	search_fields = ("name","parent__name")
	list_filter = ("state","period","isActive")
	save_as =True #replace Save and add another
	inlines = [
		SubNotificationCommentsInline,
        NotificationHistoryInline,
    ]
	save_on_top=True

admin.site.register(NotificationHistory,NotificationHistoryAdmin)	
admin.site.register(Notification,NotificationAdmin)	


	
admin.site.register(HistorySubNotificationComments)	
