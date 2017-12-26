# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-12-26 04:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_auto_20171226_0409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='update_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='update_by', to=settings.AUTH_USER_MODEL),
        ),
    ]