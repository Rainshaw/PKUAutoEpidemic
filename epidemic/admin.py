from django.contrib import admin
from . import models
# Register your models here.


class InfoAdmin(admin.ModelAdmin):
    list_display = [
        'xh',
        'pwd',
    ]


admin.site.register(models.Info, InfoAdmin)
