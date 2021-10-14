from django.contrib import admin

# Register your models here.

from app01.models import Assets

class AssetsAdmin(admin.ModelAdmin):
    list_display = ['vendor', 'soft_name', 'dep', 'pur_num', 'autho_type', 'pur_date', 'expired_date', 'demander']
    list_filter = ['vendor', 'soft_name', 'dep', 'autho_type']
    search_fields = ['soft_name']
    fields = ['vendor', 'soft_name', 'dep', 'pur_num', 'autho_type', 'pur_date', 'expired_date', 'demander']
    list_per_page = 30
 #   search_fields =



admin.site.register(Assets, AssetsAdmin)