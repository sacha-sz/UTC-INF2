# Generated by Django 3.2.9 on 2021-12-30 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sim_manager', '0002_auto_20211230_1509'),
    ]

    operations = [
        migrations.RenameField(
            model_name='simulation',
            old_name='user',
            new_name='user_id',
        ),
    ]
