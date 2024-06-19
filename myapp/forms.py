from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Customer #import model Customer that already to created in models.py file
from .models import ContactMessage
from .models import MerchantMessage


#for sign up form 
class SignUpForm (UserCreationForm):
    #here  inbuild UserCreationForm class inherit to SignUpForm class
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter First Name'}),
        max_length=30,
        required=True,
    )
    password2=forms.CharField(label='Confirm password(again)',widget=forms.PasswordInput)
    #for change label confirm password
    #password2 is name for passowrd confirmation field
    #after page view source we can see
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        # all django default field name ['username','first_name','last_name','email']

        labels={'email':'Email'}#for change email address label field name
#for login form 
#don't need to create because it is just auorization process so,it is apply in views.py
#if any class need to add then it is need add here




#for profile page form
class CustomerprofileForm(forms.ModelForm):#forms.ModelForm this in inherit to CustomerprofileForm class 
    class Meta:
        model = Customer # model Customer that already to created in models.py file
        fields=['name','locality','city','state','zipcode']


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email','phone', 'subject', 'message']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Enter your full name',
            'email': 'Enter your email address',
            'phone':'Enter your phone no',
            'subject': 'Enter the subject of your message',
            'message': 'Type your message here'
        }
        for field_name, field in self.fields.items():
            # Assign custom CSS classes to labels and fields
            field.widget.attrs['class'] = 'form-input'
            field.label = f"{field.label}"
            field.widget.attrs['placeholder'] = placeholders.get(field_name, '')



class marchentForm(forms.ModelForm):
    class Meta:
        model = MerchantMessage
        fields = ['name', 'business_or_company_name', 'business_address', 'business_category','monthly_trip','merchant_email','merchant_designation','contact_no']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Enter your full name',
            'business_or_company_name': 'Enter busniess/company name',
            'business_address': 'Enter busniess address',
           


            'merchant_email': 'Enter your marchent email',
             'merchant_designation':'Enter your position of your company',
            'contact_no': 'Eg-70********',



            
        }
        for field_name, field in self.fields.items():
            # Assign custom CSS classes to labels and fields
            field.widget.attrs['class'] = 'form-input'
            field.label = f"{field.label}"
            field.widget.attrs['placeholder'] = placeholders.get(field_name, '')