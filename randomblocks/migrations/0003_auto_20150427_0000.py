# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('randomblocks', '0002_auto_20150426_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='site',
            field=models.ForeignKey(to_field=b'subdomain', blank=True, to='pro_site.ProAccount', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blocktemplate',
            name='site',
            field=models.ForeignKey(to_field=b'subdomain', blank=True, to='pro_site.ProAccount', null=True),
            preserve_default=True,
        ),
    ]
