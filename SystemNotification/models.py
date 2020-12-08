# -*- coding: utf-8 -*-
from django.db import models
import datetime
from django.urls import reverse


class NotificationState(models.Model):
	name = models.CharField(max_length=30,db_column="name",blank=True,unique=True)
	isActive = models.BooleanField(db_column="isActive",default=True)
	red = models.IntegerField(db_column="red",default=0)
	green = models.IntegerField(db_column="green",default=0)
	blue = models.IntegerField(db_column="blue",default=0)
	back_red = models.IntegerField(db_column="back_red",default=255)
	back_green = models.IntegerField(db_column="back_green",default=255)
	back_blue = models.IntegerField(db_column="back_blue",default=255)

	def __str__(self):
		return '<State: %s: %s>' % (self.pk, self.name)
	class Meta:
		db_table = 'NotificationState'
		verbose_name_plural="Состояния задач"
		verbose_name="Состояние"
		ordering=["name",]

class GroupNotification(models.Model):
	name = models.CharField(max_length=150,db_column="name",blank=True)
	comment = models.TextField(db_column="comment",blank=True)
	isActive = models.BooleanField(db_column="isActive",default=True)
	def __str__(self):
		return '<ГруппаЗадач: %s: %s>' % (self.pk, self.name)
	class Meta:
		db_table = 'GroupNotification'
		verbose_name_plural="Группы задач"
		verbose_name="Группа задач"
		ordering=["-id",]


class Notification(models.Model):
	name = models.CharField(max_length=150,db_column="name",blank=True)
	isActive = models.BooleanField(db_column="isActive",default=True)
	parent = models.ForeignKey('GroupNotification',db_column="parent",on_delete=models.CASCADE,null=True,blank=True)
	state = models.ForeignKey('NotificationState', db_column="state",on_delete=models.PROTECT,null=True,blank=True, default=1)
	period=models.DateTimeField(db_column="period",default=datetime.datetime.now,db_index=True,blank=True)
	comment = models.TextField(db_column="comment",blank=True)
	def __str__(self):
		return '<Задача: %s: %s from %s -%s>' % (self.pk, self.name,self.parent,self.state)
	class Meta:
		db_table = 'Notification'
		verbose_name_plural="Задачи"
		verbose_name="Задача"
		ordering=["parent","-id",]
	def save(self, *args, **kwargs):
		super(Notification, self).save(*args, **kwargs)

		history,isCreated=NotificationHistory.objects.get_or_create(period=self.period,notification=self)
		history.state=self.state
		history.save()
		if isCreated:
			print("Создан новый NotificationHistory")
		else:
			print("Перезаписан существующий NotificationHistory")
	def get_absolute_url(self):
		return reverse('SystemNotification:updateObjectNotification', args=[str(self.id)])
	def test_get_absolute_url(self):
		return reverse('SystemNotification:test_pk', args=[str(self.id)])


class SubNotificationComments(models.Model):
	notification = models.ForeignKey('Notification', db_column="notification",on_delete=models.CASCADE,null=True,blank=True)
	period=models.DateTimeField(db_column="period",default=datetime.datetime.now,db_index=True,blank=True)
	comment = models.TextField(db_column="comment",blank=True)
	class Meta:
		db_table = 'SubNotificationComments'
		verbose_name_plural="Комментарии задач"
		verbose_name="Комментария к задаче"
		ordering=["-period"]
	def save(self, *args, **kwargs):
		super(SubNotificationComments, self).save(*args, **kwargs)
		history=HistorySubNotificationComments()
		history.notificationComment=self;
		history.comment=self.comment;
		history.save()

class HistorySubNotificationComments(models.Model):
	notificationComment = models.ForeignKey('SubNotificationComments', db_column="notificationComment",on_delete=models.CASCADE,null=True,blank=True)
	comment = models.TextField(db_column="comment",blank=True)
	period=models.DateTimeField(db_column="period",default=datetime.datetime.now,db_index=True,blank=True)
	class Meta:
		db_table = 'HistorySubNotificationComments'
		verbose_name_plural="Истории изменений комментов задач"
		verbose_name="История изменений комментов задачи"
		ordering=["-period"]

class NotificationHistory(models.Model):
	period=models.DateTimeField(db_column="period",default=datetime.datetime.now,db_index=True,blank=True)
	notification = models.ForeignKey('Notification', db_column="notification",on_delete=models.CASCADE,null=True,blank=True)
	state = models.ForeignKey('NotificationState', db_column="state",on_delete=models.PROTECT,null=True,blank=True)
	def __str__(self):
		return '<История: %s: %s |%s-%s|>' % (self.pk, self.period,self.notification,self.state)
	class Meta:
		db_table = 'NotificationHistory'
		verbose_name_plural="Истории изменения"
		verbose_name="История"
		ordering=["-notification","-period"]
		unique_together = [['period', 'notification']]



w="""
from django.db.models.signals import pre_save
from django.dispatch import receiver
print("Create pre_save for Notification.")
@receiver(pre_save, sender=Notification)
def after_save_Notification(sender, **kwargs):
	n=kwargs['instance']

	history,isCreated=NotificationHistory.objects.get_or_create(period=n.period,notification=n)
	history.state=n.state
	history.save()
	if isCreated:
		print("Создан новый NotificationHistory")
	else:
		print("Перезаписан существующий NotificationHistory")
"""