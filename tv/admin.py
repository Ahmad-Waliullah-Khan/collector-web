from django.contrib import admin

from .models import Shows

@admin.register(Shows)
class ShowAdmin(admin.ModelAdmin):
    list_display = (
        'show_title', 'status', 'collected_on', 'watching','started_watching_on',
        'completed_watching_on', 'seasons_watched', 'user', 'created_at', 'updated_at'
        )
