from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name="home_page"),
    path('check_price', views.check_price, name='check_price'),
    # path('servics/',views.servics,name="servics_page"),


    path('signup_using_django/', views.Signup_using_django, name='Signup_Using_Django'),
    path('login_using_django/', views.Login_using_django, name='Login_Using_Django'),
    # path('profile_using_django/', views.Profile_using_django, name='Profile_Using_Django'),#for function
    path('profile_using_django/', views.Profile_using_django.as_view(), name='Profile_Using_Django'),#for class

    path('logout_using_django/', views.Logout_using_django, name='Logout_Using_Django'),
    # path('logout_using_django/', views.Logout_using_django, name='Logout_Using_Django'),
    path('address_using_django/', views.Address_using_django, name='Address_Using_Django'),
    path('order_using_django/', views.Order_using_django, name='Order_Using_Django'),
    path('about/',views.about,name='About'),

path('privacy_policy/',views.privacy_policy,name="Privacy_Policy"),
    path('term_condition/',views.term_condition,name='Term_Condition'),


    path('contact_us/', views.Contact_us, name='Contact_US'),
    path('faq_page/', views.Faq_page, name='Faq_Page'),


    path('marchent_page/', views.Marchent_page, name='Marchent_Page'),


path('servics/', views.servics, name="servics_page"),
path('servics1/', views.servics1, name="servics_page1"),
path('servics2/',views.servics2,name='servics_page2'),
    
path('check_delivery_availability/', views.check_delivery_availability, name='check_delivery_availability'),
]
