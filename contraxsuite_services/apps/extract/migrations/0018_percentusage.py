# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-20 20:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0003_auto_20170818_0632'),
        ('extract', '0017_ratiousage'),
    ]

    operations = [
        migrations.CreateModel(
            name='PercentUsage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('amount', models.FloatField(blank=True, null=True)),
                ('amount_str', models.CharField(blank=True, max_length=150, null=True)),
                ('unit_type', models.CharField(db_index=True, max_length=20)),
                ('total', models.FloatField(blank=True, null=True)),
                ('text_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='document.TextUnit')),
            ],
            options={
                'ordering': ('text_unit', 'unit_type', '-amount'),
            },
        ),
    ]
