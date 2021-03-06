# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-08-18 04:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_comments_reply_for'),
        ('log', '0008_userprofile_email_activated'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notifs', to='blog.Comments'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='type',
            field=models.CharField(choices=[('like_notification', 'like_notification'), ('comment_notification', 'comment_notification'), ('message_notification', 'message_notification'), ('mention_notification', 'mention_notification')], max_length=200),
        ),
    ]
