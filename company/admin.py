from django.contrib import admin
from django.db.models.query import QuerySet

from .models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        'user_id',
        'name',
        'phone',
        'is_verified',
    )
    list_filter = ('is_verified', 'phone', 'name')
    search_fields = (
        'user_id',
        'name',
        'phone'
    )
    list_editable = ('is_verified',)
    list_per_page = 25
    actions = ['mark_as_verified', 'mark_as_not_verified']

    def mark_as_verified(self, _, queryset: QuerySet):
        queryset.update(is_verified=True)

    mark_as_verified.short_description = "Mark selected companies verified as true"

    def mark_as_not_verified(self, _, queryset: QuerySet):
        queryset.update(is_verified=False)

    mark_as_not_verified.short_description = "Mark selected companies verified as false"