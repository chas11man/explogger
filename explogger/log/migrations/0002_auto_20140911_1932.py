# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lens',
            name='shutter_speed_max',
        ),
        migrations.RemoveField(
            model_name='lens',
            name='shutter_speed_min',
        ),
        migrations.AddField(
            model_name='camera',
            name='shutter_speed_max',
            field=models.CharField(default='', max_length=4, choices=[(b'4000', b'4000'), (b'3000', b'3000'), (b'1000', b'1000'), (b'500', b'500'), (b'250', b'250'), (b'125', b'125'), (b'100', b'100'), (b'60', b'60'), (b'30', b'30'), (b'15', b'15'), (b'8', b'8'), (b'4', b'4'), (b'2', b'2'), (b'1"', b'1"'), (b'2"', b'2"'), (b'4"', b'4"'), (b'8"', b'8"'), (b'15"', b'15"'), (b'30"', b'30"'), (b'B', b'Bulb')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='camera',
            name='shutter_speed_min',
            field=models.CharField(default='', max_length=4, choices=[(b'4000', b'4000'), (b'3000', b'3000'), (b'1000', b'1000'), (b'500', b'500'), (b'250', b'250'), (b'125', b'125'), (b'100', b'100'), (b'60', b'60'), (b'30', b'30'), (b'15', b'15'), (b'8', b'8'), (b'4', b'4'), (b'2', b'2'), (b'1"', b'1"'), (b'2"', b'2"'), (b'4"', b'4"'), (b'8"', b'8"'), (b'15"', b'15"'), (b'30"', b'30"'), (b'B', b'Bulb')]),
            preserve_default=False,
        ),
    ]
