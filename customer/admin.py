from django.contrib import admin
from django.db.models.query import QuerySet

from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'user_id',
        'first_name',
        'phone',
        'is_verified',
    )
    list_filter = ('first_name', 'phone', 'is_verified')
    search_fields = (
        'user_id',
        'first_name',
        'phone'
    )
    list_editable = ('is_verified',)
    list_per_page = 25
    actions = ['mark_as_verified', 'mark_as_not_verified']

    def mark_as_verified(self, _, queryset: QuerySet):
        queryset.update(is_verified=True)

    mark_as_verified.short_description = "Mark selected customers verified as true"

    def mark_as_not_verified(self, _, queryset: QuerySet):
        queryset.update(is_verified=False)

    mark_as_not_verified.short_description = "Mark selected customers verified as false"

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
