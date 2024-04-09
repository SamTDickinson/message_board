from django.contrib import admin
from . import models


class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember


class GroupAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_filter = ['name', 'slug', 'description']
    list_display = ['name', 'slug', 'description']
    list_editable = ['slug', 'description']


admin.site.register(models.Group, GroupAdmin)
