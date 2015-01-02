# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('predictCenter', '0003_auto_20141227_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstock',
            name='owner',
            field=models.ForeignKey(related_name='userStock', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
