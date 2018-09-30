# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-30 09:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myimage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='name',
        ),
        migrations.AddField(
            model_name='image',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='location',
            field=models.CharField(choices=[('Nairobi', 'Nairobi'), ('Lagos', 'Lagos'), ('Moscow', 'Moscow'), ('St.peterburg', 'St.peterburg'), ('Abuja', 'Abuja'), ('Yola', 'Yola')], default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('comics', 'comics'), ('general', 'general'), ('regular', 'regular')], max_length=30),
        ),
    ]
