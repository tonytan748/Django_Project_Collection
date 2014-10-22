from django.contrib import admin

from models import ManagementList,ManagementItem

class ManagementListAdmin(admin.ModelAdmin):
	fields=('itemname',)

class ManagementItemAdmin(admin.ModelAdmin):
	fields=('user','management_item','create_date')

admin.site.register(ManagementList,ManagementListAdmin)
admin.site.register(ManagementItem,ManagementItemAdmin)
