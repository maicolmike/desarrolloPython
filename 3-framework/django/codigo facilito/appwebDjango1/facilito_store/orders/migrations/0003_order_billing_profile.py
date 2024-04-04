# Generated by Django 4.2.3 on 2023-10-11 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billing_profiles', '0001_initial'),
        ('orders', '0002_order_promo_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='billing_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='billing_profiles.billingprofile'),
        ),
    ]
