# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-06 09:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('luas', models.CharField(max_length=255)),
                ('fasilitas', models.CharField(max_length=255)),
            ],
        ),
    ]
