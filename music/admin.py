from django.contrib import admin

from .models import Music

@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'artist', 'album', 'collected_on', 'user', 'created_at', 'updated_at'
        )
