# Generated by Django 5.0.7 on 2024-08-05 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goodmeal_app', '0005_rename_title_recipe_recipe_remove_recipe_ingredients_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='Recipe',
            new_name='recipe',
        ),
    ]
