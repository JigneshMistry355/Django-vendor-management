# Generated by Django 5.0.4 on 2024-05-06 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendorPurchaseOrder', '0003_delete_performancemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='acknowledgment_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='delivery_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='issue_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='quantity',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='status',
            field=models.CharField(default='Pending', max_length=50),
        ),
    ]
