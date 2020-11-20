# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2020-11-09 10:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GroupNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, db_column=b'name', max_length=150)),
                ('comment', models.TextField(blank=True, db_column=b'comment')),
                ('isActive', models.BooleanField(db_column=b'isActive', default=True)),
            ],
            options={
                'ordering': ['-id'],
                'db_table': 'GroupNotification',
                'verbose_name': '\u0413\u0440\u0443\u043f\u043f\u0430 \u0437\u0430\u0434\u0430\u0447',
                'verbose_name_plural': '\u0413\u0440\u0443\u043f\u043f\u044b \u0437\u0430\u0434\u0430\u0447',
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, db_column=b'name', max_length=150)),
                ('isActive', models.BooleanField(db_column=b'isActive', default=True)),
                ('period', models.DateTimeField(blank=True, db_column=b'period', db_index=True, default=datetime.datetime(2020, 11, 9, 10, 53, 54, 273996))),
                ('parent', models.ForeignKey(blank=True, db_column=b'parent', null=True, on_delete=django.db.models.deletion.CASCADE, to='SystemNotification.GroupNotification')),
            ],
            options={
                'ordering': ['parent', '-id'],
                'db_table': 'Notification',
                'verbose_name': '\u0417\u0430\u0434\u0430\u0447\u0430',
                'verbose_name_plural': '\u0417\u0430\u0434\u0430\u0447\u0438',
            },
        ),
        migrations.CreateModel(
            name='NotificationHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.DateTimeField(blank=True, db_column=b'period', db_index=True, default=datetime.datetime(2020, 11, 9, 10, 53, 54, 274461))),
                ('notification', models.ForeignKey(blank=True, db_column=b'notification', null=True, on_delete=django.db.models.deletion.CASCADE, to='SystemNotification.Notification')),
            ],
            options={
                'ordering': ['-notification', '-period'],
                'verbose_name_plural': '\u0418\u0441\u0442\u043e\u0440\u0438\u0438 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f',
                'db_table': 'NotificationHistory',
                'verbose_name': '\u0418\u0441\u0442\u043e\u0440\u0438\u044f',
            },
        ),
        migrations.CreateModel(
            name='NotificationState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, db_column=b'name', max_length=30, unique=True)),
                ('isActive', models.BooleanField(db_column=b'isActive', default=True)),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'NotificationState',
                'verbose_name': '\u0421\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435',
                'verbose_name_plural': '\u0421\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u044f \u0437\u0430\u0434\u0430\u0447',
            },
        ),
        migrations.AddField(
            model_name='notificationhistory',
            name='state',
            field=models.ForeignKey(blank=True, db_column=b'state', null=True, on_delete=django.db.models.deletion.PROTECT, to='SystemNotification.NotificationState'),
        ),
        migrations.AddField(
            model_name='notification',
            name='state',
            field=models.ForeignKey(blank=True, db_column=b'state', default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='SystemNotification.NotificationState'),
        ),
        migrations.AlterUniqueTogether(
            name='notificationhistory',
            unique_together=set([('period', 'notification')]),
        ),
    ]