from django.contrib import admin

from .models import Games

@admin.register(Games)
class GameAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'status', 'collected_on', 'platform', 'completed', 'started_playing_on',
        'completed_playing_on', 'user', 'created_at', 'updated_at'
        )
