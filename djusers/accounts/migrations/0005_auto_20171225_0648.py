# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-12-25 06:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_activationprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activationprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
