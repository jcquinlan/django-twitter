# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-07 23:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followed_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relation', models.ManyToManyField(default=None, related_name='related_to', through='user_profile.Relation', to='user_profile.UserProfile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='relation',
            name='follower',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follows', to='user_profile.UserProfile'),
        ),
        migrations.AddField(
            model_name='relation',
            name='is_followed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followers', to='user_profile.UserProfile'),
        ),
        migrations.AlterUniqueTogether(
            name='relation',
            unique_together=set([('follower', 'is_followed')]),
        ),
    ]
