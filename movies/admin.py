from django.contrib import admin

from .models import Movies

@admin.register(Movies)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'status', 'collected_on', 'watched', 'started_watching_on',
        'completed_watching_on', 'user', 'created_at', 'updated_at'
        )
