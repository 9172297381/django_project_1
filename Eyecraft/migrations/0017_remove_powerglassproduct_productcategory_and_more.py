# Generated by Django 5.1.6 on 2025-03-03 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Eyecraft', '0016_powerglasscategory_parentcategory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='powerglassproduct',
            name='productCategory',
        ),
        migrations.DeleteModel(
            name='PowerGlassCategory',
        ),
        migrations.DeleteModel(
            name='PowerGlassProduct',
        ),
    ]
