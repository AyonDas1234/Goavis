# Generated by Django 5.0.3 on 2024-05-17 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_contactmessage_alter_customer_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='MerchantMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('business_or_company_name', models.CharField(max_length=100)),
                ('business_address', models.CharField(max_length=100)),
                ('mobile_no', models.CharField(max_length=15)),
                ('business_category', models.CharField(choices=[('Retail', 'Retail'), ('Wholesale', 'Wholesale'), ('Manufacturing', 'Manufacturing'), ('Service', 'Service'), ('Other', 'Other')], max_length=100)),
                ('monthly_trip', models.CharField(choices=[('Less than 20', 'Less than 20'), ('20-50', '20-50'), ('50-100', '50-100'), ('100-200', '100-200'), ('200+', '200+')], max_length=50)),
                ('merchant_email', models.EmailField(max_length=254)),
                ('contact_designation', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
