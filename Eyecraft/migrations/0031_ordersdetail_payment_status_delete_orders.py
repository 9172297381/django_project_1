# Generated by Django 5.1.6 on 2025-03-18 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eyecraft', '0030_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordersdetail',
            name='payment_status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('COMPLETED', 'Completed'), ('FAILED', 'Failed')], default='PENDING', max_length=20),
        ),
        migrations.DeleteModel(
            name='Orders',
        ),
    ]
