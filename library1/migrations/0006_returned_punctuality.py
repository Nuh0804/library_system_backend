# Generated by Django 4.2.4 on 2023-10-19 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library1', '0005_rename_date_to_retur_order_date_to_return'),
    ]

    operations = [
        migrations.AddField(
            model_name='returned',
            name='punctuality',
            field=models.BooleanField(default=False),
        ),
    ]
