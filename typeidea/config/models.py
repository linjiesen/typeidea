from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Link(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '刪除'),
    )

    title = models.CharField(max_length=255, verbose_name="標題")
    href = models.URLField(verbose_name="鏈接")
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name="狀態")
    weight = models.PositiveIntegerField(default=1, choices=zip(range(1, 6), range(1, 6)), verbose_name="權重", help_text="權重高展示順序靠前")
    owner = models.ForeignKey(User, verbose_name="作者")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="創建時間")

    class Meta:
        verbose_name = "友鏈"
        verbose_name_plural = verbose_name
        db_table = 'Link'


class SideBar(models.Model):
    STATUS_SHOW = 1
    STATUS_HIDE = 0
    STATUS_ITEMS = (
        (STATUS_SHOW, '展示'),
        (STATUS_HIDE, '隱藏'),
    )

    SIDE_TYPE = (
        (1, 'HTML'),
        (2, '最新文章'),
        (3, '最熱文章'),
        (4, '最近評論'),
    )

    title = models.CharField(max_length=255, verbose_name="標題")
    display_type = models.PositiveIntegerField(default=1, choices=SIDE_TYPE, verbose_name="展示類型")
    content = models.CharField(max_length=500, blank=True, verbose_name="內容", help_text="如果設置的不是HTML類型，可爲空")
    status = models.PositiveIntegerField(default=STATUS_SHOW, choices=STATUS_ITEMS, verbose_name="狀態")
    owner = models.ForeignKey(User, verbose_name="作者")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="創建時間")

    class Meta:
        verbose_name = "側邊欄 "
        verbose_name_plural = verbose_name
        db_table = 'SideBar'




