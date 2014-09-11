# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('brand', models.CharField(max_length=40)),
                ('model', models.CharField(max_length=40)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Exposure',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('f_stop', models.DecimalField(null=True, max_digits=3, decimal_places=1, choices=[(1, b'1'), (1.2, b'1.2'), (1.4, b'1.4'), (1.7, b'1.7'), (2, b'2'), (2.3, b'2.3'), (2.8, b'2.8'), (3.4, b'3.4'), (4, b'4'), (4.7, b'4.7'), (5.6, b'5.6'), (6.7, b'6.7'), (8, b'8'), (9.5, b'9.5'), (11, b'11'), (13, b'13'), (16, b'16'), (19, b'19'), (22, b'22'), (27, b'27'), (32, b'32'), (38, b'38'), (45, b'45')])),
                ('shutter_speed', models.CharField(max_length=4, choices=[(b'4000', b'4000'), (b'3000', b'3000'), (b'1000', b'1000'), (b'500', b'500'), (b'250', b'250'), (b'125', b'125'), (b'100', b'100'), (b'60', b'60'), (b'30', b'30'), (b'15', b'15'), (b'8', b'8'), (b'4', b'4'), (b'2', b'2'), (b'1"', b'1"'), (b'2"', b'2"'), (b'4"', b'4"'), (b'8"', b'8"'), (b'15"', b'15"'), (b'30"', b'30"'), (b'B', b'Bulb')])),
                ('focal_len', models.SmallIntegerField(null=True)),
                ('camera', models.ForeignKey(to='log.Camera')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40, blank=True)),
                ('iso', models.CharField(max_length=4)),
                ('exposure_count', models.SmallIntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lens',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('brand', models.CharField(max_length=40)),
                ('f_stop_min', models.DecimalField(null=True, max_digits=3, decimal_places=1, choices=[(1, b'1'), (1.2, b'1.2'), (1.4, b'1.4'), (1.7, b'1.7'), (2, b'2'), (2.3, b'2.3'), (2.8, b'2.8'), (3.4, b'3.4'), (4, b'4'), (4.7, b'4.7'), (5.6, b'5.6'), (6.7, b'6.7'), (8, b'8'), (9.5, b'9.5'), (11, b'11'), (13, b'13'), (16, b'16'), (19, b'19'), (22, b'22'), (27, b'27'), (32, b'32'), (38, b'38'), (45, b'45')])),
                ('f_stop_max', models.DecimalField(null=True, max_digits=3, decimal_places=1, choices=[(1, b'1'), (1.2, b'1.2'), (1.4, b'1.4'), (1.7, b'1.7'), (2, b'2'), (2.3, b'2.3'), (2.8, b'2.8'), (3.4, b'3.4'), (4, b'4'), (4.7, b'4.7'), (5.6, b'5.6'), (6.7, b'6.7'), (8, b'8'), (9.5, b'9.5'), (11, b'11'), (13, b'13'), (16, b'16'), (19, b'19'), (22, b'22'), (27, b'27'), (32, b'32'), (38, b'38'), (45, b'45')])),
                ('shutter_speed_min', models.CharField(max_length=4, choices=[(b'4000', b'4000'), (b'3000', b'3000'), (b'1000', b'1000'), (b'500', b'500'), (b'250', b'250'), (b'125', b'125'), (b'100', b'100'), (b'60', b'60'), (b'30', b'30'), (b'15', b'15'), (b'8', b'8'), (b'4', b'4'), (b'2', b'2'), (b'1"', b'1"'), (b'2"', b'2"'), (b'4"', b'4"'), (b'8"', b'8"'), (b'15"', b'15"'), (b'30"', b'30"'), (b'B', b'Bulb')])),
                ('shutter_speed_max', models.CharField(max_length=4, choices=[(b'4000', b'4000'), (b'3000', b'3000'), (b'1000', b'1000'), (b'500', b'500'), (b'250', b'250'), (b'125', b'125'), (b'100', b'100'), (b'60', b'60'), (b'30', b'30'), (b'15', b'15'), (b'8', b'8'), (b'4', b'4'), (b'2', b'2'), (b'1"', b'1"'), (b'2"', b'2"'), (b'4"', b'4"'), (b'8"', b'8"'), (b'15"', b'15"'), (b'30"', b'30"'), (b'B', b'Bulb')])),
                ('focal_len_min', models.SmallIntegerField(null=True)),
                ('focal_len_max', models.SmallIntegerField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='exposure',
            name='film',
            field=models.ForeignKey(to='log.Film'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='exposure',
            name='lens',
            field=models.ForeignKey(to='log.Lens'),
            preserve_default=True,
        ),
    ]
