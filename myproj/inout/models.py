from django.db import models
from django.contrib import admin
from django.core.validators import int_list_validator
# Create your models here.
class user_ticket(models.Model):
    username=models.CharField(max_length=64)
    ticketnum=models.IntegerField()
    first_row=models.CharField(max_length=100)
    second_row=models.CharField(max_length=100)
    third_row=models.CharField(max_length=100)
class save_random_number(models.Model):
    Random_Number=models.IntegerField()

class status_user(models.Model):
     first_row=models.CharField(max_length=100)
     second_row=models.CharField(max_length=100)
     third_row=models.CharField(max_length=100)
     full_house=models.CharField(max_length=100)
     juldi_five=models.CharField(max_length=100)
     corner=models.CharField(max_length=100)
class status(models.Model):
    user_status=models.CharField(max_length=500)

class NewsAdmin(admin.ModelAdmin):
    list_display=['user_status']

admin.site.register(status,NewsAdmin)


admin.site.register(user_ticket)
admin.site.register(save_random_number)
admin.site.register(status_user)
