from django.contrib import admin
from devotional.models import Devotional


class DevotionalAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']


admin.site.register(Devotional, DevotionalAdmin)
