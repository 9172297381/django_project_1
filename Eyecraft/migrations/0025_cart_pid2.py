# Generated by Django 5.1.6 on 2025-03-11 11:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eyecraft', '0024_customer_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='pid2',
            field=models.ForeignKey(blank=True, db_column='pid2', null=True, on_delete=django.db.models.deletion.CASCADE, to='Eyecraft.powerglassproduct'),
        ),
    ]
