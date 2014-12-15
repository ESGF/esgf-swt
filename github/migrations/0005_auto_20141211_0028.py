# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('github', '0004_auto_20141211_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='solution',
            field=models.ForeignKey(blank=True, to='github.Solution', null=True),
            preserve_default=True,
        ),
    ]
