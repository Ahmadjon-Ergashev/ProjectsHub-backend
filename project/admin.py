from django.contrib import admin
from django.db.models.query import QuerySet

from .models import Project, Tag


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'website',
        'cost',
        'is_verified',
    )
    list_filter = ('name', 'cost', 'is_verified')
    search_fields = (
        'name',
        'website',
        'cost'
    )
    list_editable = ('is_verified',)
    list_per_page = 25
    actions = ['mark_as_verified', 'mark_as_not_verified']

    def mark_as_verified(self, _, queryset: QuerySet):
        queryset.update(is_verified=True)

    mark_as_verified.short_description = "Mark selected Projects verified as true"

    def mark_as_not_verified(self, _, queryset: QuerySet):
        queryset.update(is_verified=False)

    mark_as_not_verified.short_description = "Mark selected Projects verified as false"

admin.site.register(Tag)
