# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pro_site', '0003_auto_20150424_1207'),
        ('randomblocks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='block',
            name='site',
            field=models.ForeignKey(default=b'', to_field=b'subdomain', blank=True, to='pro_site.ProAccount'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blocktemplate',
            name='site',
            field=models.ForeignKey(default=b'', to_field=b'subdomain', blank=True, to='pro_site.ProAccount'),
            preserve_default=True,
        ),
    ]
