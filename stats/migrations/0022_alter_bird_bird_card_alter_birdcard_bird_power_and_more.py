# Generated by Django 4.0.6 on 2022-07-30 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0021_alter_game_winner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bird',
            name='bird_card',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.birdcard'),
        ),
        migrations.AlterField(
            model_name='birdcard',
            name='bird_power',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stats.birdpower'),
        ),
        migrations.AlterField(
            model_name='playergame',
            name='forest_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bird_forest_1', to='stats.bird'),
        ),
        migrations.AlterField(
            model_name='playergame',
            name='forest_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bird_forest_2', to='stats.bird'),
        ),
        migrations.AlterField(
            model_name='playergame',
            name='forest_3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bird_forest_3', to='stats.bird'),
        ),
        migrations.AlterField(
            model_name='playergame',
            name='forest_4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bird_forest_4', to='stats.bird'),
        ),
        migrations.AlterField(
            model_name='playergame',
            name='forest_5',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bird_forest_5', to='stats.bird'),
        ),
        migrations.AlterField(
            model_name='playergame',
            name='plain_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bird_plain_1', to='stats.bird'),
        ),
        migrations.AlterField(
            model_name='playergame',
            name='plain_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bird_plain_2', to='stats.bird'),
        ),
        migrations.AlterField(
            model_name='playergame',
            name='plain_3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bird_plain_3', to='stats.bird'),
        ),
        migrations.AlterField(
            model_name='playergame',
            name='plain_4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bird_plain_4', to='stats.bird'),
        ),
        migrations.AlterField(
            model_name='playergame',
            name='plain_5',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bird_plain_5', to='stats.bird'),
        ),
        migrations.AlterField(
            model_name='playergame',
            name='swamp_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bird_swamp_1', to='stats.bird'),
        ),
        migrations.AlterField(
            model_name='playergame',
            name='swamp_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bird_swamp_2', to='stats.bird'),
        ),
        migrations.AlterField(
            model_name='playergame',
            name='swamp_3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bird_swamp_3', to='stats.bird'),
        ),
        migrations.AlterField(
            model_name='playergame',
            name='swamp_4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bird_swamp_4', to='stats.bird'),
        ),
        migrations.AlterField(
            model_name='playergame',
            name='swamp_5',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bird_swamp_5', to='stats.bird'),
        ),
        migrations.AlterField(
            model_name='playergame',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stats.user'),
        ),
    ]
