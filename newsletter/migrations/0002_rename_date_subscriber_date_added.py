# Generated by Django 3.2 on 2022-06-07 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscriber',
            old_name='date',
            new_name='date_added',
        ),
    ]
