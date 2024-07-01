from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from .models import MyModel,pricecalculation
from geopy.distance import geodesic
from geopy.geocoders import Nominatim

from django.http import JsonResponse

import time
import random
from django.utils import timezone
from datetime import timedelta

from django.shortcuts import render,redirect,HttpResponseRedirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm #import inherit class for UserCreationForm  inbulid class in djnago

from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #import inbulid AuthenticationForm class for login

from django.contrib.auth import authenticate,login,logout

from django.views import View  # Base class for custom views
from .forms import CustomerprofileForm  # Import your form
#CustomerprofileForm this custom class  for profile page that already have in forms.py
from .models import Customer #Customer this custom model for profile page that already have in models.py





from django.core.mail import send_mail
from .forms import ContactForm
from .models import ContactMessage
from django.conf import settings


from .forms import marchentForm
from .models import MerchantMessage




from .models import Service1,Service2

# Create your views here.
# def home(request):


#     return render(request,'myapp/home.html')
# def home(request):
    #   if request.method=='GET':
    #       PickUpLocation=request.GET.get('pickUpLocation')
    #       DropOffLocation=request.GET.get('dropOffLocation')
    #       if PickUpLocation and DropOffLocation:
    #           MyModel.objects.create(pickup_address=PickUpLocation,dropoff_address =DropOffLocation)
    #         #   return redirect ("success page")
    #         #   address1 = "Uluberia Railway Station"
    #         #   address2 = "58 Gate "

    #         #   distance = calculate_distance(address1, address2)
    #           distance = calculate_distance(PickUpLocation, DropOffLocation)
              
    #           if distance is not None:
    #               print(f"Distance between {PickUpLocation} and {DropOffLocation} is {distance:.2f} kilometers.")
    #               print(f"so, total price {distance * 10:.2f} Rs.")
    #           else:
    #             print("One or both addresses could not be geocoded.")

              

    #           return HttpResponse (f"Distance between {PickUpLocation} and {DropOffLocation} is {distance:.2f} kilometers.\n so, total price {distance * 10:.2f} Rs.")
    #       else:
    #         #   template1=loader.get_template("final_form.html",{'error_message': 'Please provide both name and last name'})
      
    #         #   return HttpResponse(template1.render())
    #           return render(request, 'myapp/home.html', {'error_message': 'Please provide both name and title'})

      
    # # return render(request, "final_form.html")
    #   else:
    #     #   return render(request, 'final_form.html')
    #       return HttpResponseNotAllowed(['GET'])

# def home(request):
#     if request.method == 'GET':
#         pickup_pincode = request.GET.get('pickupPincode')
#         dropoff_pincode = request.GET.get('dropoffPincode')
        
#         # Fetch price based on pickup and dropoff pincodes
#         try:
#            price_obj = pricecalculation.objects.filter(pickup_pincode1=pickup_pincode, dropoff_pincode2=dropoff_pincode).first()
#            price = price_obj.price
#            pickup_pincode=price_obj.pickup_pincode1
#            pickup_address=price_obj.pickup_address1
#            dropoff_pincode=price_obj.dropoff_pincode2
#            dropoff_address=price_obj.dropoff_address2
#            dis=price_obj.distance


#           #  return JsonResponse({'price': price})
          
#         except AttributeError:
#               return render(request, 'myapp/home.html',{'name':request.user,})
            
            
#                     #  return HttpResponse("Price not found for the given pincodes.", status=404)

        
#         if price is not None:
#             print("pickup pincode:-",pickup_pincode)
#             print("pickup address:-",pickup_address)

#             print(f"{price:.2f} Rs.")
            
            
#             # return HttpResponse (f"distance between {pickup_address} for it's pincode {pickup_pincode} and {dropoff_address} for it's pincode {dropoff_pincode}is {dis} kilometer. so,{price:.2f} Rs.")
#             return render(request,'myapp/home.html',{"output":price,'name':request.user,})
#         else:
#             return render(request, 'myapp/home.html', {'error_message': 'Price not found.','name':request.user,})
#               # return HttpResponse (f"Distance between {PickUpLocation} and {DropOffLocation} is {distance:.2f} kilometers.\n so, total price {distance * 10:.2f} Rs.")
        
#     else:
#         return HttpResponseNotAllowed(['GET'])
def home(request):
    return render(request, 'myapp/home.html', {'name': request.user})

def check_price(request):
    if request.method == 'GET':
        pickup_pincode = request.GET.get('pickupPincode')
        dropoff_pincode = request.GET.get('dropoffPincode')

        if pickup_pincode and dropoff_pincode:
            try:
                price_obj = pricecalculation.objects.filter(pickup_pincode1=pickup_pincode, dropoff_pincode2=dropoff_pincode).first()
                if price_obj:
                    price = price_obj.price
                    pickup_address = price_obj.pickup_address1
                    dropoff_address = price_obj.dropoff_address2
                    dis = price_obj.distance

                    result = {
                        'price': f"{price:.2f} Rs.",
                        'pickup_pincode': pickup_pincode,
                        'pickup_address': pickup_address,
                        'dropoff_pincode': dropoff_pincode,
                        'dropoff_address': dropoff_address,
                        'distance': dis
                    }
                    return JsonResponse(result)
                else:
                    return JsonResponse({'error': 'Delivery not available for the given pincodes.'}, status=404)
            except AttributeError:
                return JsonResponse({'error': 'Invalid data.'}, status=400)
        else:
            return JsonResponse({'error': 'Missing pincodes.'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=405)
# def get_coordinates(address):
#     geocoder = Nominatim(user_agent="MyGeocoder", timeout=10)
#     location = geocoder.geocode(address, exactly_one=False)
#     print(location)
#     if location:
#         for loc in location:
#             print("Latitude:", loc.latitude)
#             print("Longitude:", loc.longitude)
#             return loc.latitude, loc.longitude
#     else:
#         return None, None

# def calculate_distance(address1, address2):
#     lat1, lon1 = get_coordinates(address1)
#     lat2, lon2 = get_coordinates(address2)
#     if lat1 is not None and lon1 is not None and lat2 is not None and lon2 is not None:
#         coord1 = (lat1, lon1)
#         coord2 = (lat2, lon2)
#         distance = geodesic(coord1, coord2).kilometers
#         return distance
#     else:
#         return None


def servics(request):
                  return render(request, 'myapp/servics.html',{ 'name':request.user,})













# Create your views here.
def Signup_using_django(request):
#normal
    # if request.method=='POST':
    #     # fm =UserCreationForm(request.POST)
    #     fm =SignUpForm(request.POST)

    #     if fm.is_valid():
    #         messages.success(request,"Account created Sucessfully!!")
    #         fm.save()
    # else:
    #     #  fm=UserCreationForm()
    #      fm=SignUpForm()

    # return render(request,'myapp/signup.html',{'form':fm})

#this is for if any user already loged in then it will not show signups page

    if not request.user.is_authenticated:

                      if request.method=='POST':
                          # fm =UserCreationForm(request.POST)
                          fm =SignUpForm(request.POST)

                          if fm.is_valid():
                              messages.success(request,"Account created Sucessfully!!")
                              fm.save()
                      else:
                          #  fm=UserCreationForm()
                           fm=SignUpForm()

                      return render(request,'myapp/signup.html',{'form':fm})

    else:
        return HttpResponseRedirect('/profile_using_django/')

          
          

def Login_using_django(request):
#normal

    # if request.method=="POST":
    #     fm=AuthenticationForm(request=request,data=request.POST)
    #     if fm.is_valid():
    #         uname=fm.cleaned_data['username']
    #         upass=fm.cleaned_data['password']
    #         user=authenticate(username=uname,password=upass)
    #         if user is not None:
    #             login(request,user)
    #             messages.success(request,"logeed in succesfully!!")
    #             return HttpResponseRedirect('/profile_using_django/')
    # else:
    #     fm=AuthenticationForm()
    
    
    # return render(request,'myapp/login.html',{'form':fm})
    
#this is for if any user already loged in then it will not show login page
    if not request.user.is_authenticated:
       if request.method=="POST":
              fm=AuthenticationForm(request=request,data=request.POST)
              if fm.is_valid():
                        uname=fm.cleaned_data['username']
                        upass=fm.cleaned_data['password']
                        user=authenticate(username=uname,password=upass)
                        if user is not None:
                            login(request,user)
                            messages.success(request,"logeed in succesfully!!")
                            return HttpResponseRedirect('/profile_using_django/')
       else:
           fm=AuthenticationForm()
       return render(request,'myapp/login.html',{'form':fm})
    else:
        return HttpResponseRedirect('/profile_using_django/')

   
    



# def Profile_using_django(request):
#     #normal
#     # return render(request,'myapp/profile.html',{'name':request.user})
    

#     #this is for ,actually if any user not loged in then profile page will not showing 
#     if request.user.is_authenticated:
           
#            return render(request,'myapp/profile.html',{'name':request.user})
#     else:
#             return HttpResponseRedirect('/login_using_django/')

#for profile page views
class Profile_using_django(View):
      def get(self,request):
            
            if request.user.is_authenticated:
                        form=CustomerprofileForm()
                        return render(request,'myapp/profile.html',
                                      {'name':request.user,
                                       'form':form,
                                      'active_tab': 'profile',
                                       })
            else:
                return HttpResponseRedirect('/login_using_django/')
                  
      def post(self,request):
            if request.user.is_authenticated:
                  form =CustomerprofileForm(request.POST)
                  if form.is_valid():
                        usr=request.user #for current user means, this address will save current user
                        name=form.cleaned_data['name']
                        locality=form.cleaned_data['locality']
                        city=form.cleaned_data['city']
                        state=form.cleaned_data['state']
                        zipcode=form.cleaned_data['zipcode']
                        reg=Customer(user=usr,name=name,locality=locality,city=city,state=state,zipcode=zipcode)
                        reg.save()
                        messages.success(request,"update successfull")
                  return render(request,'myapp/profile.html',{
                        'name':request.user,
                        'form':form, 
                        'active_tab': 'profile',})
            else:
                return HttpResponseRedirect('/login_using_django/')


           
    


def Logout_using_django(request):
    logout(request)
    return HttpResponseRedirect('/login_using_django/')

def Address_using_django(request):
    if request.user.is_authenticated:
        add = Customer.objects.filter(user=request.user)#Customer this is custom model that have in models.py and based on this it will filter with current user
        return render(request, 'myapp/address.html', {
              'name':request.user,
              'add': add, 
              'active_tab': 'address',})
    else:
        return HttpResponseRedirect('/login_using_django/')
    

def Order_using_django(request):
    if request.user.is_authenticated:
        orderA= Service1.objects.filter(user=request.user)#Customer this is custom model that have in models.py and based on this it will filter with current user
        SchduleA= Service2.objects.filter(user=request.user)#Customer this is custom model that have in models.py and based on this it will filter with current user
        
       
        return render(request, 'myapp/orders.html', {
              'name':request.user,
              'orderA': orderA,
              'SchduleA': SchduleA, 
              
              'active_tab': 'order',})
    else:
        return HttpResponseRedirect('/login_using_django/')


def Contact_us(request):
     
    if request.method == 'POST':
        form = ContactForm(request.POST)  # Create form with POST data
        if form.is_valid():  # Check if the form is valid
            # Get the user's data from the form
            user_email = form.cleaned_data['email']
            user_name = form.cleaned_data['name']
            phone_no=form.cleaned_data['phone']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Save the data to the database
            form.save()
            # Save data to the database
            contact_message = form.save()

            # Compose email content
            # email_subject = f"New Contact Us Message: {contact_message.subject}"
            # email_body = f"""
            # You have a new message from {contact_message.name} ({contact_message.email}):
            
            # Subject: {contact_message.subject}
            # Message: {contact_message.message}
            # """
            email_subject = f"New Contact Message from {user_name}: {subject}"
            email_body = f"Message from {user_name} ({user_email}) ({phone_no}):\n\n{message}"
            # Send email to admin
            # send_mail(
            #     email_subject,
            #     email_body,
            #     from_email=settings.EMAIL_HOST_USER,
            #     recipient_list=[settings.ADMIN_EMAIL],  # Admin email
            # )
            send_mail(
                email_subject,
                email_body,
                from_email=user_email,  # From email address is user's email
                recipient_list=[settings.ADMIN_EMAIL],  # Admin email
            )
            messages.success(request,"message sent successfull")

            # Send the email
            # email.send()

            # Redirect to a success page
            return HttpResponseRedirect('/contact_us/')
    else:
        form = ContactForm()  # Display empty form for GET requests

    return render(request, 'myapp/contact_us.html', {'form': form, 'name':request.user})  # Render form




def term_condition(request):
    return render(request,'myapp/terms and condition.html')



def Faq_page(request):
     return render(request,'myapp/faq.html')



def Marchent_page(request):
     
    if request.method == 'POST':
        form = marchentForm(request.POST)  # Create form with POST data
        if form.is_valid():  # Check if the form is valid
            # Get the user's data from the form
            merchant_email = form.cleaned_data['merchant_email']
            merchant_name = form.cleaned_data['name']
            merchant_business_or_company_name= form.cleaned_data['business_or_company_name']
            merchant_busniess_address= form.cleaned_data['business_address']
            merchant_business_category= form.cleaned_data['business_category']
            merchant_monthly_trip= form.cleaned_data['monthly_trip']
            merchant_designation= form.cleaned_data['merchant_designation']
            contact_no= form.cleaned_data['contact_no']



            

            # Save the data to the database
            form.save()
            # Save data to the database
            marchent_message = form.save()

            # Compose email content
            # email_subject = f"New Contact Us Message: {contact_message.subject}"
            # email_body = f"""
            # You have a new message from {contact_message.name} ({contact_message.email}):
            
            # Subject: {contact_message.subject}
            # Message: {contact_message.message}
            # """
            email_subject = f"New Contact Message from {merchant_name}"
            email_body = f"Message from {merchant_name} ({merchant_email}):\n\n{merchant_business_or_company_name}\n\n{merchant_busniess_address}\n\n{merchant_business_category}\n\n{merchant_monthly_trip}\n\n{merchant_designation}\n\n{contact_no}"
            # Send email to admin
            # send_mail(
            #     email_subject,
            #     email_body,
            #     from_email=settings.EMAIL_HOST_USER,
            #     recipient_list=[settings.ADMIN_EMAIL],  # Admin email
            # )
            send_mail(
                email_subject,
                email_body,
                from_email=merchant_email,  # From email address is marchent's email
                recipient_list=[settings.ADMIN_EMAIL],  # Admin email
            )
            messages.success(request,"message sent successfull")

            # Send the email
            # email.send()

            # Redirect to a success page
            return HttpResponseRedirect('/marchent_page/')
    else:
        form = marchentForm()  # Display empty form for GET requests

    return render(request, 'myapp/merchant.html', {'form': form, 'name':request.user})  # Render form

def generate_unique_order_id():
    
    random_num = random.randint(10000, 9999999)  # Generate a random digit number
    order_id = f"{random_num}"  # Combine timestamp and random number
    return order_id

def get_ist_time():
    # Get current UTC time
    utc_time = timezone.now()
    # Add 5 hours and 30 minutes to convert to IST
    ist_time = utc_time + timedelta(hours=5, minutes=30)
    return ist_time




def servics1(request):
   if request.user.is_authenticated:
    
    if request.method == 'POST':
        name=request.POST.get('name')
        weight=request.POST.get('weight')
        pickupAddress=request.POST.get('pickupAddress')
        pickupPincode=request.POST.get('pickupPincode')
        pickupMobile=request.POST.get('pickupMobile')
        deliveryAddress=request.POST.get('deliveryAddress')
        deliveryPincode=request.POST.get('deliveryPincode')
        deliveryMobile=request.POST.get('deliveryMobile')
        sendingType=request.POST.get('sendingType')
        secureParcel=request.POST.get('secureParcel')
        paymentType=request.POST.get('paymentType')
        delivery_price=request.POST.get('delivery_price')
        # Generate unique order ID
        order_id = generate_unique_order_id()
        date_ordered=get_ist_time() 
        

        if pickupPincode and deliveryPincode:
            try:
                price_obj = pricecalculation.objects.filter(pickup_pincode1=pickupPincode, dropoff_pincode2=deliveryPincode).first()
                if price_obj:
                    price = price_obj.price
                    pickup_address = price_obj.pickup_address1
                    dropoff_address = price_obj.dropoff_address2
                    dis = price_obj.distance

                    result = {
                        'price': f"{price:.2f} Rs.",
                        'pickup_pincode': pickupPincode,
                        'pickup_address': pickup_address,
                        'dropoff_pincode': deliveryPincode,
                        'dropoff_address': dropoff_address,
                        'distance': dis
                    }
                    # return JsonResponse(result)
                    print(price)
                else:
                    # return JsonResponse({'error': 'Delivery not available for the given pincodes.'}, status=404)
                    print('Delivery not available for the given pincodes')
            except AttributeError:

                # return JsonResponse({'error': 'Invalid data.'}, status=400)
                print('Invalid data')
        else:
            # return JsonResponse({'error': 'Missing pincodes.'}, status=400)
            print('Missing pincodes')
        user=Service1.objects.create(
            name=name,
            weight=weight,
            pickupAddress=pickupAddress,
            pickupPincode=pickupPincode,
            pickupMobile=pickupMobile,
            deliveryAddress=deliveryAddress,
            deliveryPincode=deliveryPincode,
            deliveryMobile=deliveryMobile,
            sendingType=sendingType,
            secureParcel=secureParcel,
            paymentType=paymentType,
            delivery_price=price,
            order_id=order_id,
            date_ordered=date_ordered,
            user=request.user
        )
        user_email = request.user.email
        email_subject = f"New order delivery Message from {name}"
        email_body = (f" A order is confirm by {name} and email id :- ({user_email}):\n\n"
        f"Order Id:-{order_id}\n\n"
        f"Total weight :-{weight}\n\n"
        f"Pickupaddress:-{pickupAddress}\n\n"
        f"Pickuppincode:-{pickupPincode}\n\n"
         f"pickupMobile:-{pickupMobile}\n\n"
          f"pickuppincode:-{pickupPincode}\n\n"
           f"DeliveryAddress:-{deliveryAddress}\n\n"
            f"DeliveryPincode:-{deliveryPincode}\n\n"
             f"DeliveryMobile:-{deliveryMobile}\n\n"
              f"SendingType:-{sendingType}\n\n"
              f"SecureParcel:-{secureParcel}\n\n"

             f"PaymentType:-{paymentType}\n\n"
             f"price:-{price}\n\n"
             
             f"Ordered Date:-{date_ordered}\n\n"


              
        )
        recipient_list = [settings.ADMIN_EMAIL, 'Personalimportantfile100@gmail.com']
        send_mail(
                email_subject,
                email_body,
                from_email=user_email,  # From email address is marchent's email
                recipient_list=recipient_list,  # Admin email
            )
        messages.success(request,"Congratulations Order Confirmed")

        

        return redirect('/servics1/')

    return render(request, 'myapp/servics1.html',{ 'name':request.user,})
   else:
     return HttpResponseRedirect('/login_using_django/')

  
def servics2(request):
   if request.user.is_authenticated:
  
    if request.method == 'POST':
        name1=request.POST.get('name1')
        weight1=request.POST.get('weight1')
        pickupAddress1=request.POST.get('pickupAddress1')
        pickupPincode1=request.POST.get('pickupPincode1')
        pickupMobile1=request.POST.get('pickupMobile1')
        deliveryAddress1=request.POST.get('deliveryAddress1')
        deliveryPincode1=request.POST.get('deliveryPincode1')
        deliveryMobile1=request.POST.get('deliveryMobile1')
        departDate=request.POST.get('departDate')
        arriveDate=request.POST.get('arriveDate')
        sendingType1=request.POST.get('sendingType1')
        secureParcel1=request.POST.get('secureParcel1')
        paymentType1=request.POST.get('paymentType1')
        order_id = generate_unique_order_id()
        date_ordered1=get_ist_time() 

        if pickupPincode1 and deliveryPincode1:
            try:
                price_obj = pricecalculation.objects.filter(pickup_pincode1=pickupPincode1, dropoff_pincode2=deliveryPincode1).first()
                if price_obj:
                    price = price_obj.price
                    pickup_address = price_obj.pickup_address1
                    dropoff_address = price_obj.dropoff_address2
                    dis = price_obj.distance

                    result = {
                        'price': f"{price:.2f} Rs.",
                        'pickup_pincode': pickupPincode1,
                        'pickup_address': pickup_address,
                        'dropoff_pincode': deliveryPincode1,
                        'dropoff_address': dropoff_address,
                        'distance': dis
                    }
                    # return JsonResponse(result)
                    print(price)
                else:
                    # return JsonResponse({'error': 'Delivery not available for the given pincodes.'}, status=404)
                    print('Delivery not available for the given pincodes')
            except AttributeError:

                # return JsonResponse({'error': 'Invalid data.'}, status=400)
                print('Invalid data')
        else:
            # return JsonResponse({'error': 'Missing pincodes.'}, status=400)
            print('Missing pincodes')

        user=Service2.objects.create(
            name1=name1,
            weight1=weight1,
            pickupAddress1=pickupAddress1,
            pickupPincode1=pickupPincode1,
            pickupMobile1=pickupMobile1,
            deliveryAddress1=deliveryAddress1,
            deliveryPincode1=deliveryPincode1,
            deliveryMobile1=deliveryMobile1,
            departDate=departDate,
            arriveDate=arriveDate,
            sendingType1=sendingType1,
            secureParcel1=secureParcel1,
            paymentType1=paymentType1,
            delivery_price1=price,
            order_id1=order_id,
            date_ordered1=date_ordered1,
            user=request.user
        )
        user_email = request.user.email
        email_subject = f"New Schedule order Message from {name1}"
        email_body = (f" A order is confirm by {name1} and email id :- ({user_email}):\n\n"
        f"Order Id:-{order_id}\n\n"
        f"Total weight :-{weight1}\n\n"
        f"Pickupaddress:-{pickupAddress1}\n\n"
        f"Pickuppincode:-{pickupPincode1}\n\n"
         f"pickupMobile:-{pickupMobile1}\n\n"
          f"pickuppincode:-{pickupPincode1}\n\n"
           f"DeliveryAddress:-{deliveryAddress1}\n\n"
            f"DeliveryPincode:-{deliveryPincode1}\n\n"
             f"DeliveryMobile:-{deliveryMobile1}\n\n"
              f"SendingType:-{sendingType1}\n\n"
              f"SecureParcel:-{secureParcel1}\n\n"
              f"DepartDate:-{departDate}\n\n"
              f"ArriveDate:-{arriveDate}\n\n"


             f"PaymentType:-{paymentType1}\n\n"
             f"price:-{price}\n\n"
             
             f"Ordered Date:-{date_ordered1}\n\n"


              
        )
        send_mail(
                email_subject,
                email_body,
                from_email=user_email,  # From email address is marchent's email
                recipient_list=[settings.ADMIN_EMAIL],  # Admin email
            )
        messages.success(request,"Congratulations Order Schedule  Confirmed")

        return redirect('/servics2/')
    return render(request,'myapp/servics2.html',{ 'name':request.user,})
   else:
     return HttpResponseRedirect('/login_using_django/')

@csrf_exempt  # Temporarily add this for debugging
def check_delivery_availability(request):
    print('check_delivery_availability called')  # Debugging statement
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest' and request.method == 'POST':
        pickup_pincode = request.POST.get('pickupPincode1')
        delivery_pincode = request.POST.get('deliveryPincode1')
        print('Received pickupPincode1:', pickup_pincode, 'deliveryPincode1:', delivery_pincode)  # Debugging statement

        # Check if the delivery is available for the given pickup pincode and delivery pincode
        price_obj = pricecalculation.objects.filter(pickup_pincode1=pickup_pincode, dropoff_pincode2=delivery_pincode).first()

        if price_obj:
            response = {
                'available': True,
                'message': f'Delivery is available from pickup pincode {pickup_pincode} to delivery pincode {delivery_pincode}.',
                'price': price_obj.price  # Return the price directly
            }
        else:
            response = {
                'available': False,
                'message': f'Delivery is not available for the given pincode combination.',
                'price': None  # Set price to null when delivery is not available
            }
        return JsonResponse(response)
    return JsonResponse({'available': False, 'message': 'Invalid request.'})

def about(request):
    return render(request,'myapp/aboutus.html',{ 'name':request.user,})

def privacy_policy(request):
    return render(request,'myapp/privacypolicy.html',{ 'name':request.user,})
