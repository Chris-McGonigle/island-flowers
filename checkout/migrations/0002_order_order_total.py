# Generated by Django 3.2 on 2022-06-01 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
