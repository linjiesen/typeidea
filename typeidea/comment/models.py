from django.db import models

from blog.models import Post
# Create your models here.


class Comment(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '刪除'),
    )

    target = models.ForeignKey(Post, verbose_name="評論目標")
    content = models.CharField(max_length=2000, verbose_name="內容")
    nickname = models.CharField(max_length=50, verbose_name="昵稱")
    website = models.URLField(verbose_name="網站")
    email = models.EmailField(verbose_name="郵箱")
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name="狀態")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="創建時間")

    class Meta:
        verbose_name = "評論"
        verbose_name_plural = verbose_name
        db_table = 'Comment'
