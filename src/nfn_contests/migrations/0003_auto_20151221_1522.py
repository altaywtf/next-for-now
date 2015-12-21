# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-21 13:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nfn_contests', '0002_auto_20151220_1639'),
    ]

    operations = [
        migrations.CreateModel(
            name='Winner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='submission',
            name='is_winner',
        ),
        migrations.AlterField(
            model_name='contest',
            name='image',
            field=models.ImageField(default='deneme', upload_to='contests'),
        ),
        migrations.AddField(
            model_name='winner',
            name='contest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nfn_contests.Contest'),
        ),
        migrations.AddField(
            model_name='winner',
            name='winner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nfn_contests.Submission'),
        ),
    ]
