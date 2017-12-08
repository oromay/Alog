# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-08 20:50
from __future__ import unicode_literals

import apply.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('second_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('email', models.CharField(blank=True, max_length=100, verbose_name='Почта')),
            ],
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(blank=True, upload_to=apply.models.upload_location, verbose_name='Проект')),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apply.Apply')),
            ],
        ),
    ]