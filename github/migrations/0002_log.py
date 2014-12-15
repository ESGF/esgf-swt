# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('github', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.CharField(unique=True, max_length=4096)),
                ('browser_id', models.ForeignKey(to='github.Browser')),
                ('group_id', models.ForeignKey(to='github.Group')),
                ('issue_id', models.ForeignKey(to='github.Issues')),
                ('location_id', models.ForeignKey(to='github.Location')),
                ('site_id', models.ForeignKey(to='github.Site')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
