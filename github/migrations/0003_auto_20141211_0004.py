# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('github', '0002_log'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='github',
            field=models.URLField(max_length=1024, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='group',
            name='poc',
            field=models.EmailField(max_length=512, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='site',
            name='poc',
            field=models.EmailField(max_length=512, blank=True),
            preserve_default=True,
        ),
    ]
