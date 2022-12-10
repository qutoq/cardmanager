from django.contrib import admin
from .models import *


class OperationInline(admin.TabularInline):
    model = Operation


class CardAdmin(admin.ModelAdmin):
    list_display = ['series', 'number', 'status']
    inlines = [OperationInline]


admin.site.register(Card, CardAdmin)
