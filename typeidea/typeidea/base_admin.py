from django.contrib import admin


class BaseOwnerAdmin(admin.ModelAdmin):
    """
    1.用來自動補充文章、分類、標籤、側邊欄、友鏈這些Model的owner字段
    2.用來針對queryset過濾當前用戶的數據
    """
    exclude = ('owner',)

    def get_queryset(self, request):
        qs = super(BaseOwnerAdmin, self).get_queryset(request)
        return qs.filter(owner=request.user)

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(BaseOwnerAdmin, self).save_model(request, obj, form, change)
