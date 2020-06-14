from django.contrib.admin import AdminSite


class CustomSite(AdminSite):
    site_header = 'Typeidea'
    site_title = 'Typeidea Manage platform'
    index_title = '首頁'


custom_site = CustomSite(name='cus_admin')
