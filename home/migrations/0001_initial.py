# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-30 21:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='WikiArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('pageid', models.IntegerField()),
                ('links', models.ManyToManyField(to='home.ArticleLink')),
            ],
        ),
        migrations.CreateModel(
            name='WikiLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200, unique=True)),
                ('article', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.WikiLink')),
            ],
        ),
        migrations.AddField(
            model_name='articlelink',
            name='link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.WikiLink'),
        ),
    ]