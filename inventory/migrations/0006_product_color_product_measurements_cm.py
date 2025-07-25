# Generated by Django 4.2.13 on 2025-05-30 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_remove_invoice_customer_email_invoice_home_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.CharField(blank=True, help_text="The color of the product (e.g., 'Red', 'Blue', 'Assorted').", max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='measurements_cm',
            field=models.CharField(blank=True, help_text="Measurements of the product in CM (e.g., '10x5x2 cm' or 'Diameter: 15cm').", max_length=100, null=True),
        ),
    ]
