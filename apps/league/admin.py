from django.contrib import admin

from apps.league.models import League

@admin.register(League)
class LeagueAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'day_reward', 'day_reward_lose', 'week_reward',
        'des',
    )
