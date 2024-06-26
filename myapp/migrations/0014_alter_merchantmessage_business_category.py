# Generated by Django 5.0.3 on 2024-05-30 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_rename_contact_designation_merchantmessage_merchant_designation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchantmessage',
            name='business_category',
            field=models.CharField(choices=[('Retail', 'Apparels, Lifestyle'), ('Service', 'Food, Meals, Catering'), ('Retail', 'Cake, Bakery, Dairy, Sweets, Chocolate'), ('Retail', 'Frozen foods, Icecream, Desserts'), ('Retail', 'Gadgets & Electronics'), ('Retail', 'Gifts & Toys'), ('Retail', 'Florist'), ('Retail', 'Groceries'), ('Retail', 'Meat, Fish, Egg'), ('Retail', 'Fresh F & V'), ('Retail', 'Handicrafts, Artisans'), ('Retail', 'Pharma & Medical'), ('Service', 'Health & Wellness'), ('Service', 'E-commerce'), ('Retail', 'Home Decor'), ('Retail', 'Pet'), ('Retail', 'Retail'), ('Wholesale', 'Wholesale'), ('Manufacturing', 'Manufacturing'), ('Service', 'Service'), ('Other', 'Other')], max_length=100),
        ),
    ]
