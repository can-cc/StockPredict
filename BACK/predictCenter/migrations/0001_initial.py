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
            name='HotStock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('created', 'status'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stockName', models.CharField(max_length=100)),
                ('symbol', models.CharField(unique=True, max_length=50, db_tablespace=b'indexes', db_index=True)),
                ('IPOyear', models.CharField(max_length=20, null=True, blank=True)),
                ('sector', models.CharField(max_length=100, null=True, blank=True)),
                ('industry', models.CharField(max_length=100, null=True, blank=True)),
                ('SE', models.CharField(max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-created',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StockData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('stock', models.ForeignKey(related_name='data', to='predictCenter.Stock')),
            ],
            options={
                'ordering': ('created',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StockPrediction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('predict', models.FloatField(default=b'0.0')),
                ('predictRst', models.IntegerField(null=True, blank=True)),
                ('predictExpTime', models.IntegerField()),
                ('adjClose', models.FloatField()),
                ('timeOutAdjClose', models.FloatField(null=True, blank=True)),
                ('earnings', models.FloatField(null=True, blank=True)),
                ('stock', models.ForeignKey(related_name='prediction', to='predictCenter.Stock')),
            ],
            options={
                'ordering': ('-created',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserStock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('stock', models.ForeignKey(to='predictCenter.Stock')),
                ('user', models.ForeignKey(related_name='stock', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created',),
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='hotstock',
            name='stock',
            field=models.ForeignKey(to='predictCenter.Stock'),
            preserve_default=True,
        ),
    ]
