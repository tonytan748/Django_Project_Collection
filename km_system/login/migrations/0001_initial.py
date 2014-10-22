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
            name='ManagementItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('management_item', models.CharField(default=b'PO', max_length=20, choices=[(b'SUPPLIER', b'supplier'), (b'MATERIAL', b'material'), (b'PROJECT', b'project'), (b'PO', b'po'), (b'GR', b'gr'), (b'ISSUE', b'issue')])),
                ('create_date', models.CharField(max_length=100)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
