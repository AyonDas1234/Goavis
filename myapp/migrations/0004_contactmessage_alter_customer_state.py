# Generated by Django 5.0.3 on 2024-04-27 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('J', 'Jammu and Kashmir'), ('L', 'Ladakh'), ('H', 'Himachal Pradesh'), ('P', 'Punjab'), ('CH', 'Chandigarh'), ('H', 'Haryana'), ('N', 'NCT of Delhi'), ('U', 'Uttarakhand'), ('U', 'Uttar Pradesh'), ('WB', 'West Bengal'), ('B', 'Bihar'), ('O', 'Odisha'), ('JH', 'Jharkhand'), ('SK', 'Sikkim'), ('A', 'Arunachal Pradesh'), ('AS', 'Assam'), ('M', 'Manipur'), ('MG', 'Meghalaya'), ('MZ', 'Mizoram'), ('NL', 'Nagaland'), ('T', 'Tripura'), ('MP', 'Madhya Pradesh'), ('CG', 'Chhattisgarh'), ('RJ', 'Rajasthan'), ('GJ', 'Gujarat'), ('MH', 'Maharashtra'), ('GA', 'Goa'), ('KA', 'Karnataka'), ('AP', 'Andhra Pradesh'), ('TS', 'Telangana'), ('TN', 'Tamil Nadu'), ('KL', 'Kerala'), ('PY', 'Puducherry'), ('LD', 'Lakshadweep')], max_length=50),
        ),
    ]
