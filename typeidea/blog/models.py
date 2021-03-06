from django.contrib.auth.models import User
from django.db import models

import mistune
# Create your models here.

class Category(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '刪除'),
    )

    name = models.CharField(max_length=50, verbose_name="姓名")
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name="狀態")
    is_nav = models.BooleanField(default=False, verbose_name="是否爲導航")
    owner = models.ForeignKey(User, verbose_name="作者", on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="創建時間")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '分類'
        verbose_name_plural = verbose_name
        db_table = 'Category'

    @classmethod
    def get_navs(cls):
        categories = cls.objects.filter(status=cls.STATUS_NORMAL)
        nav_categories = []
        normal_categories = []
        for cate in categories:
            if cate.is_nav:
                nav_categories.append(cate)
            else:
                normal_categories.append(cate)

        return {
            'navs': nav_categories,
            'categories': normal_categories,
        }


class Tag(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '刪除'),
    )

    name = models.CharField(max_length=10, verbose_name="名稱")
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name="狀態")
    owner = models.ForeignKey(User, verbose_name="作者", on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="創建時間")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "標籤"
        verbose_name_plural = verbose_name
        db_table = 'Tag'


class Post(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_DRAFT = 2
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '刪除'),
        (STATUS_DRAFT, '草稿'),
    )

    title = models.CharField(max_length=255, verbose_name="標題")
    desc = models.CharField(max_length=1024, blank=True, verbose_name="摘要")
    content = models.TextField(verbose_name="正文", help_text="正文必須爲MarkDown格式")
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name="狀態")
    category = models.ForeignKey(Category, verbose_name="分類", on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, verbose_name="標籤")
    owner = models.ForeignKey(User, verbose_name="作者", on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="創建時間")
    content_html = models.TextField(verbose_name="正文html代碼", blank=True, editable=False)
    pv = models.PositiveIntegerField(default=1)
    uv = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']
        verbose_name = "文章"
        verbose_name_plural = verbose_name
        db_table = 'Post'

    @staticmethod
    def get_by_tag(tag_id):
        try:
            tag = Tag.objects.get(id=tag_id)
        except Tag.DoesNotExist:
            tag = None
            post_list = []
        else:
            post_list = tag.post_set.filter(status=Post.STATUS_NORMAL).select_related('owner', 'category')

        return post_list, tag

    @staticmethod
    def get_by_category(category_id):
        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            category = None
            post_list = []
        else:
            post_list = category.post_set.filter(status=Post.STATUS_NORMAL).select_related('owner', 'category')

        return post_list, category

    @classmethod
    def latest_posts(cls):
        query_set = cls.objects.filter(status=cls.STATUS_NORMAL)
        return query_set

    @classmethod
    def hot_posts(cls):
        return cls.objects.filter(status=cls.STATUS_NORMAL).order_by('-pv')

    def save(self, *args, **kwargs):
        self.content_html = mistune.markdown(self.content)
        super().save(*args, **kwargs)
