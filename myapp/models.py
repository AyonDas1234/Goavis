from django.db import models
import random
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

# from django.db import models

class MyModel(models.Model):
    pickup_address = models.CharField(max_length=100)
    dropoff_address = models.CharField(max_length=100)

class pricecalculation(models.Model):
     pickup_pincode1 = models.CharField(max_length=100)
     pickup_address1 = models.CharField(max_length=100)
     dropoff_pincode2 = models.CharField(max_length=100)
     dropoff_address2 = models.CharField(max_length=100)
     distance = models.IntegerField()
     price = models.IntegerField()





##for profile page form
# Create your models here.
STATE_CHOICE = (
    # North India
    ('J', 'Jammu and Kashmir'),
    ('L', 'Ladakh'),
    ('H', 'Himachal Pradesh'),
    ('P', 'Punjab'),
    ('CH', 'Chandigarh'),
    ('H', 'Haryana'),
    ('N', 'NCT of Delhi'),
    ('U', 'Uttarakhand'),
    ('U', 'Uttar Pradesh'),

    # East India
    ('WB', 'West Bengal'),
    ('B', 'Bihar'),
    ('O', 'Odisha'),
    ('JH', 'Jharkhand'),
    ('SK', 'Sikkim'),

    # Northeast India
    ('A', 'Arunachal Pradesh'),
    ('AS', 'Assam'),
    ('M', 'Manipur'),
    ('MG', 'Meghalaya'),
    ('MZ', 'Mizoram'),
    ('NL', 'Nagaland'),
    ('T', 'Tripura'),

    # Central India
    ('MP', 'Madhya Pradesh'),
    ('CG', 'Chhattisgarh'),

    # West India
    ('RJ', 'Rajasthan'),
    ('GJ', 'Gujarat'),
    ('MH', 'Maharashtra'),
    ('GA', 'Goa'),

    # South India
    ('KA', 'Karnataka'),
    ('AP', 'Andhra Pradesh'),
    ('TS', 'Telangana'),
    ('TN', 'Tamil Nadu'),
    ('KL', 'Kerala'),
    ('PY', 'Puducherry'),
    # ('AN', 'Andaman and Nicobar Islands'),

    # Union Territories
    ('LD', 'Lakshadweep'),
    # ('DN', 'Dadra and Nagar Haveli and Daman and Diu'),
)

class Customer(models.Model):#Customer this custom model for profile page
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    locality=models.CharField(max_length=200)
    city=models.CharField(max_length=50)
    zipcode=models.IntegerField()
    state=models.CharField(choices=STATE_CHOICE,max_length=50)
     

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone=models.IntegerField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} about '{self.subject}'"
    


monthly_choice = (
    ('Less than 20', 'Less than 20'),
    ('20-50', '20-50'),
    ('50-100', '50-100'),
    ('100-200', '100-200'),
    ('200+', '200+')
)

business_category_choice = (
    ('Retail', 'Apparels, Lifestyle'),
    ('Service', 'Food, Meals, Catering'),
    ('Retail', 'Cake, Bakery, Dairy, Sweets, Chocolate'),
    ('Retail', 'Frozen foods, Icecream, Desserts'),
    ('Retail', 'Gadgets & Electronics'),
    ('Retail', 'Gifts & Toys'),
    ('Retail', 'Florist'),
    ('Retail', 'Groceries'),
    ('Retail', 'Meat, Fish, Egg'),
    ('Retail', 'Fresh F & V'),
    ('Retail', 'Handicrafts, Artisans'),
    ('Retail', 'Pharma & Medical'),
    ('Service', 'Health & Wellness'),
    ('Service', 'E-commerce'),
    ('Retail', 'Home Decor'),
    ('Retail', 'Pet'),
    ('Retail', 'Retail'),
    ('Wholesale', 'Wholesale'),
    ('Manufacturing', 'Manufacturing'),
    ('Service', 'Service'),
    ('Other', 'Other')
)

class MerchantMessage(models.Model):
    name = models.CharField(max_length=100)
    business_or_company_name = models.CharField(max_length=100)
    business_address = models.CharField(max_length=100)
    
    business_category = models.CharField(choices=business_category_choice, max_length=100)
    monthly_trip = models.CharField(choices=monthly_choice, max_length=50)
    merchant_email = models.EmailField()
    merchant_designation = models.CharField(max_length=100)
    contact_no=models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Merchant Message from {self.name}"
    



order_status_choice = (
    ('Processing', 'processing'),
    ('On-Hold', 'On-Hold'),
    ('Cancel', 'Cancel'),
    ('Picked Up', 'Picked up'),
    ('Completed', 'Completed')
)

class Service1(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    weight = models.FloatField()
    pickupAddress = models.CharField(max_length=200)
    pickupPincode = models.CharField(max_length=20)
    pickupMobile = models.CharField(max_length=20)
    deliveryAddress = models.CharField(max_length=200)
    deliveryPincode = models.CharField(max_length=6)
    deliveryMobile = models.CharField(max_length=20)

    sendingType = models.CharField(max_length=100)
    secureParcel = models.CharField(max_length=100, blank=True, null=True)
    paymentType = models.CharField(max_length=100)
    delivery_price=models.IntegerField()
    order_status=models.CharField(choices=order_status_choice, max_length=50,blank=True, null=True,default='processing')
    date_ordered = models.DateTimeField(default=timezone.now)
    order_id = models.IntegerField()  
    


    # remember_me = models.BooleanField(default=False)
    def __str__(self):
        return f"Delivery Order from {self.name}"
class Service2(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name1 = models.CharField(max_length=100)
    weight1= models.FloatField()
    pickupAddress1 = models.CharField(max_length=200)
    pickupPincode1 = models.CharField(max_length=20)
    pickupMobile1 = models.CharField(max_length=20)
    deliveryAddress1 = models.CharField(max_length=200)
    deliveryPincode1 = models.CharField(max_length=6)
    deliveryMobile1 = models.CharField(max_length=20)
    departDate=models.DateTimeField()
    arriveDate=models.DateTimeField()
    sendingType1 = models.CharField(max_length=100)
    secureParcel1 = models.CharField(max_length=100, blank=True, null=True)
    paymentType1 = models.CharField(max_length=100)
    delivery_price1=models.IntegerField()
    order_status1=models.CharField(choices=order_status_choice, max_length=50,blank=True, null=True)
    date_ordered1 = models.DateTimeField(default=timezone.now)
    order_id1 = models.IntegerField()  
    def __str__(self):
        return f"Schedule Order from {self.name1}"







