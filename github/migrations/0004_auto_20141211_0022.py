# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('github', '0003_auto_20141211_0004'),
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(unique=True, max_length=1024)),
                ('group_id', models.ForeignKey(to='github.Group')),
                ('solution', models.ForeignKey(to='github.Solution', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='issues',
            name='group_id',
        ),
        migrations.RemoveField(
            model_name='issues',
            name='solution',
        ),
        migrations.RenameField(
            model_name='group',
            old_name='issue',
            new_name='issue_name',
        ),
        migrations.AlterField(
            model_name='log',
            name='issue_id',
            field=models.ForeignKey(to='github.Issue'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Issues',
        ),
    ]
