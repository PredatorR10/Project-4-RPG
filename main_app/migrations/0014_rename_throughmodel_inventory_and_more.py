# Generated by Django 4.0.3 on 2022-04-12 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0013_throughmodel_character_inventory_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ThroughModel',
            new_name='Inventory',
        ),
        migrations.RemoveField(
            model_name='character',
            name='inventory',
        ),
        migrations.AddField(
            model_name='character',
            name='inv',
            field=models.ManyToManyField(through='main_app.Inventory', to='main_app.item'),
        ),
    ]
