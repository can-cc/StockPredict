# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RechargeRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('coin', models.IntegerField()),
                ('peyment', models.CharField(max_length=30)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(related_name='RechargeRecord', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserCount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('coin', models.IntegerField()),
                ('total', models.IntegerField()),
                ('user', models.ForeignKey(related_name='UserCount', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserPredictPermission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('permissionLevel', models.IntegerField()),
                ('permissionTime', models.IntegerField()),
                ('user', models.ForeignKey(related_name='UserPredictPermission', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nickName', models.CharField(max_length=30)),
                ('photo', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('selfDescription', models.TextField(null=True, blank=True)),
                ('hometown', models.CharField(max_length=30)),
                ('nowCity', models.CharField(max_length=30)),
                ('user', models.ForeignKey(related_name='UserProfile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserSetting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.ForeignKey(related_name='UserSetting', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
