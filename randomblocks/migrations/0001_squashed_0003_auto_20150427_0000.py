# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    replaces = [('randomblocks', '0001_initial'), ('randomblocks', '0002_auto_20150426_2320'), ('randomblocks', '0003_auto_20150427_0000')]

    dependencies = [
        ('pro_site', '0003_auto_20150424_1207'),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('context', jsonfield.fields.JSONField(default=dict)),
                ('weight', models.IntegerField(default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BlockTemplate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=70)),
                ('markup', models.TextField()),
                ('site', models.ForeignKey(to_field=b'subdomain', blank=True, to='pro_site.ProAccount', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='block',
            name='template',
            field=models.ForeignKey(to='randomblocks.BlockTemplate'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='block',
            name='site',
            field=models.ForeignKey(to_field=b'subdomain', blank=True, to='pro_site.ProAccount', null=True),
            preserve_default=True,
        ),
    ]
