# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-01 07:26
from __future__ import unicode_literals

from django.db import migrations, models
import pickle

class Migration(migrations.Migration):

    dependencies = [
        ('chat_app', '0003_auto_20170927_0258'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='public_key',
            field=models.BinaryField(default=b'\x80\x03X\x01\x00\x00\x00sq\x00.'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='message',
            name='secret_key',
            field=models.BinaryField(default=b'\x80\x03X\x01\x00\x00\x00sq\x00.'),
            preserve_default=False,
        ),
    ]
    


