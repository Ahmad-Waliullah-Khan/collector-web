from django.contrib import admin

from .models import ComicBooks

@admin.register(ComicBooks)
class ComicBookAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'status', 'collected_on', 'reading', 'completed_reading', 'started_reading_on',
        'completed_reading_on', 'user', 'created_at', 'updated_at'
        )
