from django.contrib import admin

from .models import Books

@admin.register(Books)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'status', 'collected_on', 'reading', 'completed_reading', 'started_reading_on',
        'completed_reading_on', 'user', 'created_at', 'updated_at'
        )
