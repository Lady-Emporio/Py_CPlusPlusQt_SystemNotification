# Generated by Django 3.0.2 on 2020-11-08 16:47

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SystemNotification', '0018_auto_20201108_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='period',
            field=models.DateTimeField(blank=True, db_column='period', db_index=True, default=datetime.datetime(2020, 11, 8, 16, 47, 9, 221247)),
        ),
        migrations.AlterField(
            model_name='notification',
            name='state',
            field=models.ForeignKey(blank=True, db_column='state', default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='SystemNotification.NotificationState'),
        ),
        migrations.AlterField(
            model_name='notificationhistory',
            name='period',
            field=models.DateTimeField(blank=True, db_column='period', db_index=True, default=datetime.datetime(2020, 11, 8, 16, 47, 9, 221247)),
        ),
    ]
