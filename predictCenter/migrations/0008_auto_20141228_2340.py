# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predictCenter', '0007_auto_20141227_2316'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockPrediction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('stockShortName', models.CharField(max_length=100)),
                ('predict', models.CharField(default=b'unknown', max_length=20)),
                ('predictExpTime', models.IntegerField()),
            ],
            options={
                'ordering': ('created',),
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='stock',
            name='stockShortName',
            field=models.CharField(unique=True, max_length=50),
            preserve_default=True,
        ),
    ]
