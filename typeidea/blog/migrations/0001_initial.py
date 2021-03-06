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
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='姓名')),
                ('status', models.PositiveIntegerField(choices=[(1, '正常'), (0, '刪除')], default=1, verbose_name='狀態')),
                ('is_nav', models.BooleanField(default=False, verbose_name='是否爲導航')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='創建時間')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
            options={
                'verbose_name': '分類',
                'verbose_name_plural': '分類',
                'db_table': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='標題')),
                ('desc', models.CharField(blank=True, max_length=1024, verbose_name='摘要')),
                ('content', models.TextField(help_text='正文必須爲MarkDown格式', verbose_name='正文')),
                ('status', models.PositiveIntegerField(choices=[(1, '正常'), (0, '刪除'), (2, '草稿')], default=1, verbose_name='狀態')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='創建時間')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category', verbose_name='分類')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
                'db_table': 'Post',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='名稱')),
                ('status', models.PositiveIntegerField(choices=[(1, '正常'), (0, '刪除')], default=1, verbose_name='狀態')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='創建時間')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
            options={
                'verbose_name': '標籤',
                'verbose_name_plural': '標籤',
                'db_table': 'Tag',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(to='blog.Tag', verbose_name='標籤'),
        ),
    ]
