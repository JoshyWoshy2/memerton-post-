# Generated by Django 4.1.4 on 2023-01-03 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_meme_options_alter_meme_confidence'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meme',
            name='confidence',
            field=models.FloatField(default=0.0),
        ),
    ]