from django.db import models
from django.contrib import admin


class PlayerGame(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        null=True,
    )
    game = models.ForeignKey(
        'Game',
        on_delete=models.CASCADE,
        null=False,
        related_name='player_games'
    )
    bonus_point = models.IntegerField(
        default=0,
        null=False,
        verbose_name='Point des cartes bonus'
    )
    round_point = models.IntegerField(
        default=0,
        null=False,
        verbose_name='Point des fin de manches'
    )
    total_eggs = models.IntegerField(
        default=0,
        null=False,
        verbose_name="Nombre d'oeuf"
    )
    card_kept_at_beginning = models.IntegerField(
        default=3,
        null=False,
        verbose_name='Nombre de carte gardées en début de partie'
    )
    card_at_the_end = models.IntegerField(
        default=0,
        null=False,
        verbose_name='Nombre de cartes restantes en fin de partie'
    )
    food_at_the_end = models.IntegerField(
        default=3,
        null=False,
        verbose_name='Nombre de nourritures restantes en fin de partie'
    )
    forest_1 = models.ForeignKey(
        'Bird',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='bird_forest_1'
    )
    forest_2 = models.ForeignKey(
        'Bird',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='bird_forest_2'
    )
    forest_3 = models.ForeignKey(
        'Bird',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='bird_forest_3'
    )
    forest_4 = models.ForeignKey(
        'Bird',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='bird_forest_4'
    )
    forest_5 = models.ForeignKey(
        'Bird',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='bird_forest_5'
    )
    plain_1 = models.ForeignKey(
        'Bird',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='bird_plain_1'
    )
    plain_2 = models.ForeignKey(
        'Bird',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='bird_plain_2'
    )
    plain_3 = models.ForeignKey(
        'Bird',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='bird_plain_3'
    )
    plain_4 = models.ForeignKey(
        'Bird',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='bird_plain_4'
    )
    plain_5 = models.ForeignKey(
        'Bird',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='bird_plain_5'
    )
    swamp_1 = models.ForeignKey(
        'Bird',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='bird_swamp_1'
    )
    swamp_2 = models.ForeignKey(
        'Bird',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='bird_swamp_2'
    )
    swamp_3 = models.ForeignKey(
        'Bird',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='bird_swamp_3'
    )
    swamp_4 = models.ForeignKey(
        'Bird',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='bird_swamp_4'
    )
    swamp_5 = models.ForeignKey(
        'Bird',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='bird_swamp_5'
    )
    score = models.IntegerField(
        default=0,
        null=False,
        verbose_name='Total points'
    )
    engine_size = models.IntegerField(
        default=0,
        null=False,
        verbose_name='Taille du moteur'
    )

    def __str__(self):
        return f'{self.user}: {self.score} pts'


@admin.register(PlayerGame)
class PlayerGameAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'game',
        'score',
    )

    readonly_fields = (
        'score',
        'engine_size',
    )

    def has_delete_permission(self, request, obj=None):
        return False

    @admin.action(description='Compute Data')
    def compute_data(self, request, queryset):
        from stats.service.player_game_service import PlayerGameService

        for player_game in queryset:
            PlayerGameService(player_game).compute_data()

    actions = (
        compute_data,
    )


class PlayerGameInline(admin.TabularInline):
    model = PlayerGame
    fields = (
        'user',
        'bonus_point',
        'round_point',
        'total_eggs',
        'card_kept_at_beginning',
        'card_at_the_end',
        'food_at_the_end',
    )
