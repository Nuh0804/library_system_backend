# Generated by Django 4.2.4 on 2023-10-19 17:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library1', '0006_returned_punctuality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='returned',
            name='date_returned',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
