# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0002_auto_20140911_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exposure',
            name='f_stop',
            field=models.FloatField(null=True, choices=[(1, b'1'), (1.2, b'1.2'), (1.4, b'1.4'), (1.7, b'1.7'), (2, b'2'), (2.3, b'2.3'), (2.8, b'2.8'), (3.4, b'3.4'), (4, b'4'), (4.7, b'4.7'), (5.6, b'5.6'), (6.7, b'6.7'), (8, b'8'), (9.5, b'9.5'), (11, b'11'), (13, b'13'), (16, b'16'), (19, b'19'), (22, b'22'), (27, b'27'), (32, b'32'), (38, b'38'), (45, b'45')]),
        ),
        migrations.AlterField(
            model_name='lens',
            name='f_stop_max',
            field=models.FloatField(null=True, choices=[(1, b'1'), (1.2, b'1.2'), (1.4, b'1.4'), (1.7, b'1.7'), (2, b'2'), (2.3, b'2.3'), (2.8, b'2.8'), (3.4, b'3.4'), (4, b'4'), (4.7, b'4.7'), (5.6, b'5.6'), (6.7, b'6.7'), (8, b'8'), (9.5, b'9.5'), (11, b'11'), (13, b'13'), (16, b'16'), (19, b'19'), (22, b'22'), (27, b'27'), (32, b'32'), (38, b'38'), (45, b'45')]),
        ),
        migrations.AlterField(
            model_name='lens',
            name='f_stop_min',
            field=models.FloatField(null=True, choices=[(1, b'1'), (1.2, b'1.2'), (1.4, b'1.4'), (1.7, b'1.7'), (2, b'2'), (2.3, b'2.3'), (2.8, b'2.8'), (3.4, b'3.4'), (4, b'4'), (4.7, b'4.7'), (5.6, b'5.6'), (6.7, b'6.7'), (8, b'8'), (9.5, b'9.5'), (11, b'11'), (13, b'13'), (16, b'16'), (19, b'19'), (22, b'22'), (27, b'27'), (32, b'32'), (38, b'38'), (45, b'45')]),
        ),
    ]
