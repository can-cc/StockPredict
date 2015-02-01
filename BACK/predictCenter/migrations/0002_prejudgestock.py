# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predictCenter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreJudgeStock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('judgeDay', models.DateField()),
                ('dtl', models.IntegerField()),
                ('stockPrediction', models.ForeignKey(related_name='preJudge', to='predictCenter.StockPrediction')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
