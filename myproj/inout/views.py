from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from inout.forms import SignUpForm
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.core.serializers import serialize
from django.contrib.auth.models import User
import sys
from .decorators import admin_only
from .get_users import get_all_logged_in_users
from random import *

from subprocess import run,PIPE
import psutil
from inout.models import user_ticket,save_random_number,status_user,status
import json
from json import JSONEncoder
import random
import numpy as np
import sys
from tabulate import tabulate
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template import RequestContext
from inout import main
import re
import tkinter
from tkinter import messagebox

from django.http import HttpResponse
from django.template import RequestContext, Template

##def ip_address_processor(request):
##    return {'ip_address': request.META['REMOTE_ADDR']}

# def client_ip_view(request):
#     request_context = RequestContext(request)
#     request_context.push({"my_name": "Adrian"})
#     return HttpResponse(request_context)
#     # template = Template('{{ title }}: {{ ip_address }}')
#     # context = RequestContext(request, {
#     #     'title': 'Your IP Address',
#     # }, [add_variable_to_context])
#     # return HttpResponse(template.render(context))


# Create your views here.
def home_view(request):
    return render(request,'inout/home.html')


@login_required
def mygallary_view(request):
    return render(request,'inout/gallary.html')

@login_required
def myprofile_view(request):
    return render(request,'inout/profile.html')

def logout_view(request):
    return render(request,'inout/logout.html')

def signup_view(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)

        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')

    return render(request,'inout/signup.html',{'form':form})
@login_required
def generate_tickets_page_view(request):

    return render(request,'inout/generate_tickets.html')

def generate_tickets_view(request):

       inp=request.GET.get('n_tickets')

       def getTickets():
           """
           #1 - Maintain array of total_numbers between 1 and 90. Initialize ticket_array as 3x9 array of 0s
           #2 - Generate 15 random indices from the array of total_indices.
           #3 - Compute index to drop the value into based on RULE #1, RULE #2
           #4 - Remove values used in the ticket from the base array (RULE #1, RULE #2)
           #5 - Repeat till 15 numbers are populated into ticket
           #6 - Sort numbers in every column of the ticket based on RULE #3
           """

           # Create a 2D array [3x9] of 0s
           ticket_array = np.zeros((3, 9), dtype=int)
           # Create an a list of numbers from 1 to 90.
           total_numbers = [num for num in range(1, 91)]
           # Create a list of tupele of all the indices of 3x9 ticket_array . i.e (0,0),(0,1),...,(2,8)
           total_indices = [(i, j) for i in range(3) for j in range(9)]
           # Create an empty list to store 15 random indices to fill in the value.
           random_indices = []

           first_list=[1,2,3,4,5,6,7,8,9]

           second_list=[10,11,12,13,14,15,16,17,18,19]

           third_list=[20,21,22,23,24,25,26,27,28,29]

           fourth_list=[30,31,32,33,34,35,36,37,38,39]

           fifth_list=[40,41,42,43,44,45,46,47,48,49]

           sixth_list=[50,51,52,53,54,55,56,57,58,59]

           seventh_list=[60,61,62,63,64,65,66,67,68,69]

           eigth_list=[70,71,72,73,74,75,76,77,78,79]

           ninth_list=[80,81,82,83,84,85,86,87,88,89,90]


           # Generate 15 random indices that satisfies RULE #1 and store them in random_indices array.

           first_row = random.sample(total_indices[:9], 5)
           second_row = random.sample(total_indices[9:18], 5)
           third_row = random.sample(total_indices[-9:], 5)

           for i in first_row:
               random_indices.append(i)

           for i in second_row:
               random_indices.append(i)

           for i in third_row:
               random_indices.append(i)

           # Populate values in the randomly generated indices such that it satisfies RULE #2 and replace the  value of the used value in total_numbers array by 0.

           for num in random_indices:
               if num[1] == 0:
                   number = random.choice(first_list[:])
                   first_list.remove(number)
                   ticket_array[num] = number
                   total_numbers[total_numbers.index(number)] = 0


               elif num[1] == 1:
                   number = random.choice(second_list[:])
                   second_list.remove(number)
                   ticket_array[num] = number
                   total_numbers[total_numbers.index(number)] = 0
                   number = random.choice(first_list[:])
               elif num[1] == 2:
                   number = random.choice(third_list[:])

                   third_list.remove(number)
                   ticket_array[num] = number
                   total_numbers[total_numbers.index(number)] = 0
               elif num[1] == 3:
                   number = random.choice(fourth_list[:])
                   fourth_list.remove(number)
                   ticket_array[num] = number
                   total_numbers[total_numbers.index(number)] = 0
               elif num[1] == 4:
                   number = random.choice(fifth_list[:])
                   fifth_list.remove(number)
                   ticket_array[num] = number
                   total_numbers[total_numbers.index(number)] = 0
               elif num[1] == 5:
                   number = random.choice(sixth_list[:])
                   sixth_list.remove(number)
                   ticket_array[num] = number
                   total_numbers[total_numbers.index(number)] = 0
               elif num[1] == 6:
                   number = random.choice(seventh_list[:])
                   seventh_list.remove(number)
                   ticket_array[num] = number
                   total_numbers[total_numbers.index(number)] = 0
               elif num[1] == 7:
                   number = random.choice(eigth_list[:])
                   eigth_list.remove(number)
                   ticket_array[num] = number
                   total_numbers[total_numbers.index(number)] = 0
               elif num[1] == 8:
                   number = random.choice(ninth_list[:])
                   ninth_list.remove(number)
                   ticket_array[num] = number
                   total_numbers[total_numbers.index(number)] = 0

           # Sort the ticket_array column wise to satisfy the RULE #3

           for col in range(9):
               # if all the rows are filled with random number
               if(ticket_array[0][col] != 0 and ticket_array[1][col] != 0 and ticket_array[2][col] != 0):
                   for row in range(2):
                       if ticket_array[row][col] > ticket_array[row+1][col]:
                           temp = ticket_array[row][col]
                           ticket_array[row][col] = ticket_array[row+1][col]
                           ticket_array[row+1][col] = temp

               # if 1st and 2nd row are filled by random number
               elif(ticket_array[0][col] != 0 and ticket_array[1][col] != 0 and ticket_array[2][col] == 0):
                   if ticket_array[0][col] > ticket_array[1][col]:
                       temp = ticket_array[0][col]
                       ticket_array[0][col] = ticket_array[1][col]
                       ticket_array[1][col] = temp

               # if 1st and 3rd row are filled by random number
               elif(ticket_array[0][col] != 0 and ticket_array[2][col] != 0 and ticket_array[1][col] == 0):
                   if ticket_array[0][col] > ticket_array[2][col]:
                       temp = ticket_array[0][col]
                       ticket_array[0][col] = ticket_array[2][col]
                       ticket_array[2][col] = temp

               # if 2nd and 3rd rows are filled with random numbers
               elif(ticket_array[0][col] == 0 and ticket_array[1][col] != 0 and ticket_array[2][col] != 0):
                   if ticket_array[1][col] > ticket_array[2][col]:
                       temp = ticket_array[1][col]
                       ticket_array[1][col] = ticket_array[2][col]
                       ticket_array[2][col] = temp
           ##tkt=np.argwhere(ticket_array)
           ##ticket_array[ticket_array==0]=['nan']
           return ticket_array

       numberOfTickets = inp
       tickets = []
       ticket_num=[]
       for i in range(int(numberOfTickets)):

           ticket = getTickets()
           print(type(ticket))
           tickets.append(ticket)
           print(type(tickets))
           tkt_num=randint(10000,20000)
           ticket_num.append(tkt_num);
           for j in range(len(ticket)):
               if(j==0):
                   firstrow=ticket[j]
               if(j==1):
                   secondrow=ticket[j]
               else:
                   thirdrow=ticket[j]
           user_ticket.objects.create(username=request.user.username,ticketnum=tkt_num,
           first_row=firstrow,second_row=secondrow,third_row=thirdrow)
       class NumpyArrayEncoder(JSONEncoder):

             def default(self,obj):
               if isinstance(obj,np.ndarray):
                   return obj.tolist()
               return JSONEncoder.default(self,obj)

       numpyData = {"array": tickets}
       print(type(tickets))
       print(tickets)
       print(type(numpyData))
       encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
       print("Printing JSON serialized NumPy array")
       print(encodedNumpyData)

# Deserialization
       print("Decode JSON serialized NumPy array")
       decodedArrays = json.loads(encodedNumpyData)



       return JsonResponse(decodedArrays,safe=False)








@login_required
@admin_only

def active_view(request):
    users= get_all_logged_in_users()
    data= json.loads(serialize('json',users))
    return JsonResponse(data,safe=False)


def start_game_view(request):
   ##main.send_sms("6300633077","  your first row completed")
   count=range(1,91)
   ##context={}
   context={'count':count}
   ##context['count']=count

   ##request_context=RequestContext(request)
   ##request_context.push({"my_name":"Adrian"})

   return render(request,'inout/startgame.html',context)
   ##return HttpResponse(template.render(request_context))



first_list=[]
second_list=[]
third_list=[]
status_list=[]
message_list=[]


def savenumber_and_compare_view(request):
    randomNumber=request.GET.get('randomNumber')
    save_number=save_random_number.objects.create(Random_Number=randomNumber)
    rows_data=user_ticket.objects.all()
    random_data=save_random_number.objects.all()
    array1=[]
    R_Num=int(randomNumber)

    x='First Row Finished'
    y='Second Row Finished'
    z='Third Row Finished'
    xyz='Full House Finished'
    xyzz='Juldi Five Finished'
    xyzzz='Corner With Center Finished'
    first_row_message='First Row'
    second_row_message='Second Row'
    third_row_message='Third Row'
    full_house_message='Full House'
    juldi_five_message='Juldi Five'
    corner_center_message='Corner With Center'
    dict_index_number={}
    dict_Ph_No={}
    dict_Full_House_Final_List={}
    full_list=[]
    Juldi_Five_List=[]
    corner_center_list=[]
    db_save_list=[]

    for j in random_data:
         array1.append(j.Random_Number)

    print(array1)

    for i in rows_data:

          #### checking for first row #########

        if(any(item in x for item in status_list)==False):
            list1=list(re.split('\]|\[|\s',i.first_row))
            list2=[int(char) for char in list1 if char!='0' and char!='']
            f_check = all(item in array1 for item in list2)
            if f_check == True:
                first_list.append(i.username+' First Row Completed with Number '+str(R_Num))
                ##status.objects.create(user_status=i.username+' First Row Completed with Number '+str(R_Num))

         #### checking for second row #########

        if(any(item in y for item in status_list)==False):
            list1=list(re.split('\]|\[|\s',i.second_row))
            list2=[int(char) for char in list1 if char!='0' and char!='']
            s_check = all(item in array1 for item in list2)
            if s_check == True:
                second_list.append(i.username+' Second Row Completed with Number '+str(R_Num))
                ##status.objects.create(user_status=i.username+' Second Row Completed with Number '+str(R_Num))



             #### checking for third row #########

        if(any(item in z for item in status_list)==False):
             list1=list(re.split('\]|\[|\s',i.third_row))
             list2=[int(char) for char in list1 if char!='0' and char!='']
             t_check = all(item in array1 for item in list2)
             if t_check == True:
                 third_list.append(i.username+' Third Row Completed with Number '+str(R_Num))
                 ##status.objects.create(user_status=i.username+' Third Row Completed with Number '+str(R_Num))


        #### checking for Juldi five ######

        if(any(item in xyzz for item in status_list)==False):
            list1=list(re.split('\]|\[|\s',i.first_row))
            list2=list(re.split('\]|\[|\s',i.second_row))
            list3=list(re.split('\]|\[|\s',i.third_row))
            All_Rows_List=list1+list2+list3
            All_Rows_Final_List=[int(char) for char in All_Rows_List if char!='0' and char!='']
            if sum(item in array1 for item in All_Rows_Final_List)==5:
                Juldi_Five_List.append(i.username+' Juldi Five Completed with Number '+str(R_Num))
                ##status.objects.create(user_status=i.username+' Juldi Five Completed with Number '+str(R_Num))



        #### checking for Corner with center ####
        if(any(item in xyzzz for item in status_list)==False):
           list1=list(re.split('\]|\[|\s',i.first_row))
           list2=list(re.split('\]|\[|\s',i.second_row))
           list3=list(re.split('\]|\[|\s',i.third_row))
           All_Rows_List1=list1+list2+list3
           All_Rows_Final_List1=[int(char) for char in All_Rows_List1 if char!='0' and char!='']
           index_list=[0,4,7,10,14]
           result_list=[All_Rows_Final_List1[item] for item in index_list]
           if(all(item in array1 for item in result_list)==True):
               corner_center_list.append(i.username+' Corner With Center Completed with Number '+str(R_Num))
               ##status.objects.create(user_status=i.username+' Corner With Center Completed with Number '+str(R_Num))










          ### checking for full house #######

        if(any(item in xyz for item in status_list)==False):
            print("first ok")
            list1=list(re.split('\]|\[|\s',i.first_row))
            list2=list(re.split('\]|\[|\s',i.second_row))
            list3=list(re.split('\]|\[|\s',i.third_row))
            Full_House_List=list1+list2+list3
            Full_House_Final_List=[int(char) for char in Full_House_List if char!='0' and char!='']
            print(dict_Full_House_Final_List)
            ##R_Num=int(randomNumber)
            R_Num1=[R_Num]
            print(R_Num1)
            print(type(R_Num1))
            if(any(item in R_Num1 for item in Full_House_Final_List)==True):
                index_number=Full_House_Final_List.index(R_Num)
                dict_index_number[i.username]=index_number
                dict_Full_House_Final_List[i.username]=Full_House_Final_List


    if len(dict_index_number)>=1:

        sorting_list=list(dict_index_number.values())
        sort_list_without_dupliactes=list(dict.fromkeys(sorting_list))
        sort_list_without_dupliactes.sort()

        for i in sort_list_without_dupliactes:
            if len(full_list)==0:
                res = [key for key in dict_index_number if dict_index_number[key] == i]
                for username in res:
                    Full_check = all(item in array1 for item in dict_Full_House_Final_List[username])
                    if Full_check == True:
                         full_list.append(username+' Full House Completed with Number '+str(R_Num))
                         ##status.objects.create(user_status=username+' Full House Completed with Number '+str(R_Num))




       ### checks for sending message #####

    if len(first_list)>=1:
        if (any(first_row_message in item for item in message_list)==False):
            status_list.append(x)
            f_z=' and '.join([user for user in first_list])
            message_list.append("Message Sent For First Row")
            db_save_list.append(f_z)

            print(f_z)
            ##main.send_sms("9666798996",f_z)

        ##main.send_sms("9989578784",array2[0])
        ##print(array2[0])
        ##if(any(x in mystring for mystring in array2)==False):
    if len(second_list)>=1:
        if (any(second_row_message in item for item in message_list)==False):
            status_list.append(y)
            s_z=' and '.join([user for user in second_list])
            message_list.append("Message Sent For Second Row")
            db_save_list.append(s_z)

            print(s_z)
            ##main.send_sms("9666798996",s_z)


    if len(third_list)>=1:
        if (any(third_row_message in item for item in message_list)==False):
            status_list.append(z)
            t_z=' and '.join([user for user in third_list])
            message_list.append("Message Sent For Third Row")
            db_save_list.append(t_z)

            print(t_z)
            ##main.send_sms("9666798996",t_z)

    if len(full_list)>=1:
        if(any(full_house_message in item for item in message_list)==False):
            status_list.append(xyz)
            full_xyz=' and '.join([user for user in full_list])
            message_list.append("Message Sent For Full House")
            db_save_list.append(full_xyz)
            print(full_xyz)


            ##main.send_sms("9666798996",full_xyz)

    if len(Juldi_Five_List)>=1:
        if(any(juldi_five_message in item for item in message_list)==False):
            status_list.append(xyzz)
            Juldi_xyzz=' and '.join([user for user in Juldi_Five_List])
            message_list.append("Message Sent For Juldi Five")
            db_save_list.append(Juldi_xyzz)

            print(Juldi_xyzz)
            ##main.send_sms("9666798996",Juldi_xyzz)


    if len(corner_center_list)>=1:
        if(any(corner_center_message in item for item in message_list)==False):
            status_list.append(xyzzz)
            Corner_xyzzz=' and '.join([user for user in corner_center_list])
            message_list.append("Message Sent For Corner With Center")
            db_save_list.append(Corner_xyzzz)
            print(Corner_xyzzz)
            ##main.send_sms("9666798996",Corner_xyzzz)

    if len(db_save_list)>=1:
        for i in db_save_list:
            status.objects.create(user_status=i)








    data= json.loads(serialize('json',save_number))
    return JsonResponse(data,safe=False)


def deletenumber_view(request):
    save_random_number.objects.all().delete()
    status.objects.all().delete()
    user_ticket.objects.all().delete()
    first_list.clear()
    second_list.clear()
    third_list.clear()
    status_list.clear()
    message_list.clear()

def see_generated_number_view(request):
    generated_number=save_random_number.objects.all()


    data= json.loads(serialize('json',generated_number))
    return JsonResponse(data,safe=False)

def getuser_ticket_data_view(request):

    username=request.GET.get('username')

    ##print(request.session.keys())

    userdata=user_ticket.objects.filter(username__iexact=username)
    data= json.loads(serialize('json',userdata))
    return JsonResponse(data,safe=False)



def validate_username(request):
    username=request.GET.get('username')
    data={
    'is_taken':User.objects.filter(username__iexact=username).exists()
    }
    if data['is_taken']:
        data['error_message']='A user with this name already exists'
    return JsonResponse(data)


def get_user_status_view(request):
    data=status.objects.order_by('-pk')                   ## to reverse data from database.like newest to oldest record
    status_data= json.loads(serialize('json',data))
    return JsonResponse(status_data,safe=False)


# def test_view(request):
#     request.session['hello']="Hello every one"
#     return render(request,
#          'test.html',context_instance=RequestContext(request))
#     print("this is view data")

##def compare_view(request):

    # def handle_new_job(sender, **kwargs):
    #
    #     print(kwargs['raw'])


             ##print(array2)












    #
    #     if y not in array3:
    #         list2=list(re.split('\]|\[|\s',i.second_row))
    #         list3=[int(char) for char in list2 if char!='0' and char!='']
    #         check1 = all(item in array1 for item in list3)
    #         if check1 is True:
    #             array2.append(i.username+' Second Row Completed')
    #         if len(array3)>=1:
    #
    #     if z not in array3:
    #         list4=list(re.split('\]|\[|\s',i.third_row))
    #         list5=[int(char) for char in list4 if char!='0' and char!='']
    #         check2 = all(item in array1 for item in list5)
    #         if check2 is True:
    #             array2.append(i.username+' Third Row Completed')
    #
    #
    #
    #
    # if len(array3)>1:
    #     main.send_sms("9989578784",first_array[0]+' and '+first_array[1] )
    # else:
    #     main.send_sms("9989578784",first_array[0])
    # array3.append(x)
        ##print(i.username)


        ## array1.extend(j)
         ##print(array1[j])
    #     r_number=j.Random_Number
    #     array1.extend(r_number)
    #     print(r_number)
    #     print(type(r_number))
    #     print(array1)
        ##print(random_data.Random_Number)



    ##return render(request,'inout/test1.html',{'test_msg':test_msg})

# @receiver(post_save, sender=save_random_number)
# def handle_new_job(sender, **kwargs):
#
#     print(kwargs['raw'])
