"""myproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from inout import views as i
from django.contrib.auth import views as d
from inout.forms import UserLoginForm


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', i.home_view,name='home'),
    path('pictures/', i.mygallary_view),
    path('myprof/', i.myprofile_view),

    path('accounts/', include('django.contrib.auth.urls'),),
    path('logout/',i.logout_view),
    path('signup/',i.signup_view),
    path('gplay/',i.generate_tickets_page_view),
    path('gplay/ajax/get_tickets/',i.generate_tickets_view),

    path('dboard/',i.start_game_view),
    path('dboard/ajax/user_ticket_info/',i.getuser_ticket_data_view),
    ##re_path('getdata/(?P<udata>[a-zA-Z]+)',i.getuser_ticket_data_view),
    path('ajax/validate_username/',i.validate_username),
    path('dboard/ajax/active_users/',i.active_view),
    ##path('testing/',i.test_view),
    path('dboard/ajax/sessiondata/',i.savenumber_and_compare_view),
    ##path('dboard/ajax/comparedata/',i.compare_view),
    path('dboard/ajax/delete_data',i.deletenumber_view),
    path('gplay/ajax/see_generated_number',i.see_generated_number_view),
    path('gplay/ajax/get_user_status',i.get_user_status_view),

    path('pictures/ajax/see_generated_number',i.see_generated_number_view),




    ]
