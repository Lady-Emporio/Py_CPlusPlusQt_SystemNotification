# Generated by Django 3.1.3 on 2020-12-01 08:35

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
                ('name', models.CharField(blank=True, db_column='name', max_length=150)),
                ('comment', models.TextField(blank=True, db_column='comment')),
                ('isActive', models.BooleanField(db_column='isActive', default=True)),
            ],
            options={
                'verbose_name': 'Группа задач',
                'verbose_name_plural': 'Группы задач',
                'db_table': 'GroupNotification',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, db_column='name', max_length=150)),
                ('isActive', models.BooleanField(db_column='isActive', default=True)),
                ('period', models.DateTimeField(blank=True, db_column='period', db_index=True, default=datetime.datetime(2020, 12, 1, 8, 35, 46, 247734))),
                ('parent', models.ForeignKey(blank=True, db_column='parent', null=True, on_delete=django.db.models.deletion.CASCADE, to='SystemNotification.groupnotification')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
                'db_table': 'Notification',
                'ordering': ['parent', '-id'],
            },
        ),
        migrations.CreateModel(
            name='NotificationState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, db_column='name', max_length=30, unique=True)),
                ('isActive', models.BooleanField(db_column='isActive', default=True)),
                ('red', models.IntegerField(db_column='red', default=0)),
                ('green', models.IntegerField(db_column='green', default=0)),
                ('blue', models.IntegerField(db_column='blue', default=0)),
                ('back_red', models.IntegerField(db_column='back_red', default=255)),
                ('back_green', models.IntegerField(db_column='back_green', default=255)),
                ('back_blue', models.IntegerField(db_column='back_blue', default=255)),
            ],
            options={
                'verbose_name': 'Состояние',
                'verbose_name_plural': 'Состояния задач',
                'db_table': 'NotificationState',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='SubNotificationComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.DateTimeField(blank=True, db_column='period', db_index=True, default=datetime.datetime(2020, 12, 1, 8, 35, 46, 247734))),
                ('comment', models.TextField(blank=True, db_column='comment')),
                ('notification', models.ForeignKey(blank=True, db_column='notification', null=True, on_delete=django.db.models.deletion.CASCADE, to='SystemNotification.notification')),
            ],
            options={
                'verbose_name': 'Комментария к задаче',
                'verbose_name_plural': 'Комментарии задач',
                'db_table': 'SubNotificationComments',
                'ordering': ['-period'],
            },
        ),
        migrations.AddField(
            model_name='notification',
            name='state',
            field=models.ForeignKey(blank=True, db_column='state', default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='SystemNotification.notificationstate'),
        ),
        migrations.CreateModel(
            name='HistorySubNotificationComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, db_column='comment')),
                ('period', models.DateTimeField(blank=True, db_column='period', db_index=True, default=datetime.datetime(2020, 12, 1, 8, 35, 46, 248734))),
                ('notificationComment', models.ForeignKey(blank=True, db_column='notificationComment', null=True, on_delete=django.db.models.deletion.CASCADE, to='SystemNotification.subnotificationcomments')),
            ],
            options={
                'verbose_name': 'История изменений комментов задачи',
                'verbose_name_plural': 'Истории изменений комментов задач',
                'db_table': 'HistorySubNotificationComments',
                'ordering': ['-period'],
            },
        ),
        migrations.CreateModel(
            name='NotificationHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.DateTimeField(blank=True, db_column='period', db_index=True, default=datetime.datetime(2020, 12, 1, 8, 35, 46, 248734))),
                ('notification', models.ForeignKey(blank=True, db_column='notification', null=True, on_delete=django.db.models.deletion.CASCADE, to='SystemNotification.notification')),
                ('state', models.ForeignKey(blank=True, db_column='state', null=True, on_delete=django.db.models.deletion.PROTECT, to='SystemNotification.notificationstate')),
            ],
            options={
                'verbose_name': 'История',
                'verbose_name_plural': 'Истории изменения',
                'db_table': 'NotificationHistory',
                'ordering': ['-notification', '-period'],
                'unique_together': {('period', 'notification')},
            },
        ),
    ]
