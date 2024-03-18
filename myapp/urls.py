from django.urls import path
from .import views

urlpatterns =[
    path('',views.index,name="home"),
    path('about',views.about,name="about"),
    path('events',views.event,name="event"),
    path('contact',views.Contact,name="contact"),
    path('gallery',views.gallary,name="gallary"),
    path('login',views.login,name="login"),
    path('register',views.register,name="register"),
    path('forgot',views.forgot,name="forgot"),
    path('reset',views.reset,name="reset"),
    path('wedding',views.wedding,name="wedding"),
    path('mehndi',views.mehndi,name="mehndi"),
    path('sangeet',views.sangeet,name="sangeet"),
    path('haldi',views.haldi,name="haldi"),
    path('reception',views.reception,name="reception"),
    path('marraige',views.marraige,name="marraige"),
    path('birthday',views.birthday,name="birthday"),
    path('theme',views.theme,name="theme"),
    path('booking',views.Booking,name="booking"),
    path('college',views.college,name="college"),
    path('graduation',views.graduation,name="graduation"),
    path('festival',views.festival,name="festival"),
    path('fresher',views.fresher,name="fresher"),
    path('annual',views.annual,name="annual"),
    path('insert',views.insert_data,name="insert"),
    path('Checklogin',views.CheckLogin,name="checklogin"),
    path('booking_insert',views.booking_insert,name="booking_insert"),
    path('contact_insert',views.contact_data,name="contact_insert"),
    path('forgotpassword',views.forgotpassword,name="forgotpassword"),
    path('editprofile', views.editprofile, name="edit"),
    path('updateprofile',views.updateprofile,name="update"),
    path('logout',views.logout,name="logout"),
    path('payment/<int:bid>',views.Payment,name="payment"),
    path('paymentinsert',views.payment_insert,name="payment_insert")
    djkmnekdm
]