# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-31 16:53
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
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='標題')),
                ('href', models.URLField(verbose_name='鏈接')),
                ('status', models.PositiveIntegerField(choices=[(1, '正常'), (0, '刪除')], default=1, verbose_name='狀態')),
                ('weight', models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1, help_text='權重高展示順序靠前', verbose_name='權重')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='創建時間')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
            options={
                'verbose_name': '友鏈',
                'verbose_name_plural': '友鏈',
                'db_table': 'link',
            },
        ),
        migrations.CreateModel(
            name='SideBar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='標題')),
                ('display_type', models.PositiveIntegerField(choices=[(1, 'HTML'), (2, '最新文章'), (3, '最熱文章'), (4, '最近評論')], default=1, verbose_name='展示類型')),
                ('content', models.CharField(blank=True, help_text='如果設置的不是HTML類型，可爲空', max_length=500, verbose_name='內容')),
                ('status', models.PositiveIntegerField(choices=[(1, '展示'), (0, '隱藏')], default=1, verbose_name='狀態')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='創建時間')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
            options={
                'verbose_name': '側邊欄 ',
                'verbose_name_plural': '側邊欄 ',
                'db_table': 'SideBar',
            },
        ),
    ]
