# Generated by Django 5.0.4 on 2024-05-04 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendorProfile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='vendor_code',
            field=models.CharField(blank=True, max_length=50, unique=True),
        ),
    ]