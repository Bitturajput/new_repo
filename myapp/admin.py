from django.contrib import admin
from .models import *


# Register your models here.
class show_user(admin.ModelAdmin):
    list_display = ["Name","contactno","email","password"]
admin.site.register(User,show_user)


class show_category(admin.ModelAdmin):
    list_display = ["cat_name"]
admin.site.register(category,show_category)

class show_sub_category(admin.ModelAdmin):
    list_display = ["Category_Id","name"]
admin.site.register(sub_category,show_sub_category)    

class show_package(admin.ModelAdmin):
    list_display =["name","subcat_id","details","amount"]
admin.site.register(package,show_package) 

class show_booking(admin.ModelAdmin):
    list_display =["User_Id","Category","subcat","Package","First_Name","Last_Name","Phone_no","Time","Email","date","details","Location"]
admin.site.register(BOOKING,show_booking)

class show_payment(admin.ModelAdmin):
    list_display =["booking_id","type","date","amount"]
admin.site.register(payment,show_payment)  

class show_Feedback(admin.ModelAdmin):
    list_display =["User_Id","description"]
admin.site.register(Feedback,show_Feedback)

class show_contact(admin.ModelAdmin):
    list_display = ["Name","Email","Subject","Message"]
admin.site.register(contact,show_contact)

class show_card(admin.ModelAdmin):
    list_display=["User_Id","Name","card_num","Cvv","Expiry_Date","timestamp"]
admin.site.register(Card,show_card)