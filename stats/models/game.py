from django.db import models
from django.contrib import admin

from stats.models.player_game import PlayerGameInline
from stats.service.game_service import GameService

date_format = "%d %b %Y"


class Game(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    winner = models.ForeignKey(
        'PlayerGame',
        on_delete=models.CASCADE,
        null=True,
        related_name='winner',
    )

    def __str__(self):
        date = self.created_at.strftime(date_format)
        player_names = GameService.get_player_name(self)

        return f'{date}: {player_names}'

    def players(self):
        player_games = self.player_games.all()
        players = list(
            map(
                lambda player_game: player_game.user,
                player_games
            )
        )
        return players


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = (
        'get_date',
        'get_player_name',
        'winner',
    )

    readonly_fields = (
        'winner',
    )

    def has_delete_permission(self, request, obj=None):
        return False

    def get_date(self, instance):
        return instance.created_at.strftime(date_format)
    get_date.short_description = 'Date'

    def get_player_name(self, instance):
        return GameService.get_player_name(instance)
    get_player_name.short_description = 'Joueurs'

    @admin.action(description='Compute Score')
    def compute_score(self, request, queryset):
        from stats.service.game_service import GameService

        for game in queryset:
            GameService.compute_winner(game)

    actions = (
        compute_score,
    )

    inlines = (
        PlayerGameInline,
    )
