"""instagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from instagramapp.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',reg_pg),
    url(r'^reg_page/',reg_page,name='reg_page'),
    url(r'^register/',register,name='register'),
    url(r'^login_pg/',login_pg,name='login_pg'),
    url(r'^login_check/',login_check,name='login_check'),
    url(r'^userhome_pg/',userhome_pg,name='userhome_pg'),
    url(r'^loadimg/',loadimg,name='loadimg'),
    url(r'^add_post/',add_post,name='add_post'),
    url(r'^edit_profile/',edit_profile,name='edit_profile'),
    url(r'^adminhome/',adminhome,name='adminhome'),
    url(r'^logout_fn/',logout_fn,name='logout_fn'),
    url(r'^all_user_fn/',all_user_fn,name='all_user_fn'),
    url(r'^send_dealer_info_fn/',send_dealer_info_fn,name='send_dealer_info_fn'),
##    url(r'^adminhome/',adminhome,name='adminhome'),


]
