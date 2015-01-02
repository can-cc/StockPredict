# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predictCenter', '0008_auto_20141228_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotstock',
            name='stockShortName',
            field=models.CharField(unique=True, max_length=50),
            preserve_default=True,
        ),
    ]
