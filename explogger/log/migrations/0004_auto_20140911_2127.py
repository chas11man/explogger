# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('log', '0003_auto_20140911_1939'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cameras', models.ManyToManyField(to='log.Camera')),
                ('films', models.ManyToManyField(to='log.Film')),
                ('lenses', models.ManyToManyField(to='log.Lens')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='exposure',
            name='user',
            field=models.ForeignKey(to='log.UserProfile', null=True),
            preserve_default=True,
        ),
    ]
