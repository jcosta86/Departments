from django.contrib import admin
from .models import Department


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name',)
    list_display_links = ('id', 'name')


admin.site.register(Department, DepartmentAdmin)
