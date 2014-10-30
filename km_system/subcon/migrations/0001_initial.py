# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Subcon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=200)),
                ('tel', models.CharField(max_length=15)),
                ('fax', models.CharField(max_length=15)),
                ('contact', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=500)),
                ('scope_of_work', models.CharField(max_length=150)),
                ('remark', models.CharField(max_length=500)),
                ('gst_verification', models.CharField(max_length=10)),
                ('gst_reg_no', models.CharField(max_length=120)),
                ('create_by', models.CharField(default=django.contrib.auth.models.User, max_length=200)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('edit_date', models.DateTimeField(auto_now_add=True)),
                ('edit_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
