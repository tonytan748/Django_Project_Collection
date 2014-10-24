# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=200)),
                ('address', models.TextField()),
                ('product', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=120)),
                ('phone', models.CharField(max_length=50)),
                ('fax', models.CharField(max_length=50)),
                ('remark', models.TextField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('is_published', models.BooleanField(default=True)),
                ('create_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
