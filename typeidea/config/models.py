from django.contrib.auth.models import User
from django.db import models
from django.template.loader import render_to_string


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
    weight = models.PositiveIntegerField(default=1, choices=zip(range(1, 6), range(1, 6)), verbose_name="權重",
                                         help_text="權重高展示順序靠前")
    owner = models.ForeignKey(User, verbose_name="作者", on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="創建時間")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "友鏈"
        verbose_name_plural = verbose_name
        db_table = 'Link'


class SideBar(models.Model):
    DISPLAY_HTML = 1
    DISPLAY_LATEST = 2
    DISPLAY_HOT = 3
    DISPLAY_COMMENT = 4
    SIDE_TYPE = {
        (DISPLAY_HTML, 'HTML'),
        (DISPLAY_LATEST, '最新文章'),
        (DISPLAY_HOT, '最熱文章'),
        (DISPLAY_COMMENT, '最近評論'),
    }

    STATUS_SHOW = 1
    STATUS_HIDE = 0
    STATUS_ITEMS = (
        (STATUS_SHOW, '展示'),
        (STATUS_HIDE, '隱藏'),
    )

    title = models.CharField(max_length=255, verbose_name="標題")
    display_type = models.PositiveIntegerField(default=1, choices=SIDE_TYPE, verbose_name="展示類型")
    content = models.CharField(max_length=500, blank=True, verbose_name="內容", help_text="如果設置的不是HTML類型，可爲空")
    status = models.PositiveIntegerField(default=STATUS_SHOW, choices=STATUS_ITEMS, verbose_name="狀態")
    owner = models.ForeignKey(User, verbose_name="作者", on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="創建時間")

    def __str__(self):
        return self.title

    @classmethod
    def get_all(cls):
        return cls.objects.filter(status=cls.STATUS_SHOW)

    @property
    def content_html(self):
        """直接渲染模板"""
        from blog.models import Post    # 避免循環引用
        from comment.models import Comment

        result = ''
        if self.display_type == self.DISPLAY_HTML:
            result = self.content
        elif self.display_type == self.DISPLAY_LATEST:
            content = {
                'posts': Post.latest_posts()
            }
            result = render_to_string('config/blocks/sidebar_posts.html', content)
        elif self.display_type == self.DISPLAY_HOT:
            content = {
                'posts': Post.hot_posts()
            }
            result = render_to_string('config/blocks/sidebar_posts.html', content)
        elif self.display_type == self.DISPLAY_COMMENT:
            content = {
                'comments': Comment.objects.filter(status=Comment.STATUS_NORMAL)
            }
            result = render_to_string('config/blocks/sidebar_comments.html', content)
        return result

    class Meta:
        verbose_name = "側邊欄 "
        verbose_name_plural = verbose_name
        db_table = 'SideBar'
