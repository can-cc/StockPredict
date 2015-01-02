# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predictCenter', '0006_auto_20141227_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstock',
            name='userId',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
