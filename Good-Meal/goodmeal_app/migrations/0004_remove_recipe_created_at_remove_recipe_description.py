# Generated by Django 5.0.7 on 2024-08-04 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goodmeal_app', '0003_delete_tasklist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='description',
        ),
    ]
