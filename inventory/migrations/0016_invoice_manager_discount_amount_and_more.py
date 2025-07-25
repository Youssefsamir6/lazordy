# Generated by Django 5.2.1 on 2025-06-15 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0015_invoice_due_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='manager_discount_amount',
            field=models.DecimalField(decimal_places=2, default=0.0, help_text='Special discount applied by manager.', max_digits=10),
        ),
        migrations.AddField(
            model_name='invoice',
            name='manager_discount_reason',
            field=models.CharField(blank=True, help_text="Reason for the manager's special discount.", max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='notes',
            field=models.TextField(blank=True, help_text='Any additional notes for the invoice.', null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='payment_method',
            field=models.CharField(blank=True, choices=[('cash', 'Cash'), ('card', 'Card'), ('bank_transfer', 'Bank Transfer')], help_text='Method of payment.', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='terms_and_conditions',
            field=models.TextField(blank=True, help_text='Terms and conditions for this invoice.', null=True),
        ),
    ]
