# Generated by Django 4.0.6 on 2022-07-30 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0023_engine'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playergame',
            name='engine_size',
        ),
        migrations.AddField(
            model_name='playergame',
            name='engine',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stats.engine'),
        ),
    ]
