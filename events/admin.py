from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import Event, Organizer


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'event_type',
        'topic',
        'event_date',
        'event_end_date',
        'price',
        'is_published',
        'created_by',
    )

    fieldsets = (
        (None, {
            'fields': (
                ('title', 'is_published'),
            ),
        }),
        (_('Information'), {
            'fields': (
                'description',
                'event_source_url',
                'image',
                'image_source_url',
                ('event_type', 'topic'),
                ('event_date', 'event_end_date'),
                'price',
                'organizer',
                'place',
            ),
        }),
    )

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Organizer)
class OrganizerAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_by', 'created', 'modified')

    search_fields = ('name',)

    fieldsets = (
        (None, {
            'fields': (
                'name',
                'description',
            ),
        }),
    )

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)

    def has_delete_permission(self, request, obj=None):
        return False
