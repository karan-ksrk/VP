# Generated by Django 3.2 on 2021-04-14 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playerBoard', '0008_alter_player_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='isIn',
            field=models.BooleanField(),
        ),
    ]