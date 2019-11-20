# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
##from .test_network import *
from .models import *
##from models import *
from django.http import HttpResponse,JsonResponse
import json
from django.core import serializers
from django.shortcuts import render_to_response
from django.core.files.storage import FileSystemStorage
from random import random

# Python Program to Get IP Address 
import socket 
hostname = socket.gethostname() 
IPAddr = socket.gethostbyname(hostname)
# Create your views here.
def reg_pg(request):
    print ("reg_pg")
    return render(request,"registration.html",{})
def reg_page(request):
    print ("reg_page")
    return render(request,"registration.html",{})
def login_pg(request):
    print ("login_pg")
    return render(request,"login.html",{})
def adminhome(request):
    print ("adminhome")
    user_dt=register_tb.objects.filter(role='user')
    dealer_drug=dealer_info_tb.objects.all()
####################
    drug_dealer_acc_new=[]
    drug_dealer_acc_old=[]
    if request.session.has_key('us_name'):
        user_dt=register_tb.objects.filter(role='user')
        dealer_drug_view=dealer_info_tb.objects.filter(status='viewed')
        if dealer_drug_view.count()!=0:
##            obj=dealer_info_tb.objects.all().delete()
            for i in dealer_drug_view:
                drug_dealer_acc_old.append(i.id)
                print("drug_dealer_acc_old",drug_dealer_acc_old)
        for i in user_dt:
            print("i.id",i.id)
            imag_drug=image_tb.objects.filter(user_id=i.id,status='drug')
            text_drug=text_tb.objects.filter(user_id=i.id,status='drug')
##            print("image drug:",imag_drug.count())
##            print("text drug:",text_drug.count())
            if ((imag_drug.count()+text_drug.count())>5):
                print(i.name,"*********new dealer**********")
                if i.id not in drug_dealer_acc_old:
                    drug_dealer_acc_new.append(i.id)
                    obj=dealer_info_tb(
                        id=i.id,name=i.name,email=i.email,username=i.username,gender=i.gender,ipaddr=i.ipaddr,status='viewed'
                        )
                    obj.save()
            print("drug_dealer_acc_new",drug_dealer_acc_new)
        dealer_drug=dealer_info_tb.objects.all()
        print("........................dealer count...in adminhome........",dealer_drug.count())
        return render(request,"admin_home.html",{"user_dtt":user_dt,"drug_acc":dealer_drug})
####################
    return render(request,"admin_home.html",{"user_dtt":user_dt,"drug_acc":dealer_drug})
def userhome_pg(request):
    print ("userhome_pg")
    usernm=register_tb.objects.get(id=int(request.session['us_name']))
    print("userdt",usernm)
    images=image_tb.objects.filter(user_id=request.session['us_name'])
    ob=register_tb.objects.filter(id=request.session['us_name'])
    for i in images:
        for j in ob:
            print (type(i.id),type(j.id))
            if int(i.user_id)==j.id:
                print (j.name)
    print ("Images name:\n",images)
    print()
    texts=text_tb.objects.filter(user_id=request.session['us_name'])

    return render(request,"userhome.html",{"usernamee":usernm,'imag':images,"users":ob,"txts":texts})

def register(request):
    print ("in regiseter")
 
    print("Your Computer Name is:" + hostname) 
    print("Your Computer IP Address is:" + IPAddr) 
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        uname=request.POST.get("username")
        gen=request.POST.get("gender")
        paswd=request.POST.get("password")
        print ("name,email,uname,gen,paswd",name,email,uname,gen,paswd)
        user_check=register_tb.objects.filter(username=uname)
        user_check_count=user_check.count()
##        if name=="" or email=="" or uname=="" or gen=="" or paswd=="":
##            return HttpResponse("<script>alert('please fill all details successful');window.location.href='registration.html';</script>")
##        else:
        if user_check_count==0:
            u=name.replace(' ','.')         
            obj=register_tb(
                name=u.upper(),email=email,username=uname,gender=gen,password=paswd,role="user",ipaddr=IPAddr
                )
            obj.save()
            print("registerd")
            return HttpResponse("<script>alert('registration successful');window.location.href=/login_pg/;</script>")
        else:
            print("already registerd")
            return HttpResponse("<script>alert('Sorry, username already exist registration unsuccessful');window.location.href=/reg_page/;</script>")
##    return HttpResponse("<script>alert('Network error');window.location.href='registration.html';</script>")
def login_check(request):
    print ("login_check(request):")
    if request.method=="POST":
        u=request.POST.get("username")
        p=request.POST.get("password")
        print ("in login page:",u,"::::",p)
        user_data=register_tb.objects.filter(username=u,password=p)
        count=user_data.count()
        for i in user_data:
            usertype=i.role
            print("user.....",i.username,"role........",usertype)
        if count==1 and usertype=='user':
##                print "in if request.session::::::::::::",request.session['us_name']
            user_id=register_tb.objects.get(username=u,password=p)
            userid=user_id.id
            request.session['us_name']=userid
            n=request.session['us_name']
            print ("user id:::::::::::::::::::::::::::_____________________",userid)
            for i in user_data:
                usernm=i.username
                upass=i.password
            print ("username:",usernm,"password:",upass)
            images=image_tb.objects.filter(user_id=request.session['us_name'])
            texts=text_tb.objects.filter(user_id=request.session['us_name'])
            ob=register_tb.objects.filter(id=request.session['us_name'])
            for i in images:
                for j in ob:
                    print (type(i.id),type(j.id))
                    if int(i.user_id)==j.id:
                        print (j.name)
            print ("Images name:\n",images)
            for i in texts:
                for j in ob:
                    print (type(i.id),type(j.id))
                    if int(i.user_id)==j.id:
                        print (j.name)
            print ("text post:\n",texts)            
##            obj2=dealer_info_tb.objects.get(id=userid)
##            obj2.ipaddr=user_id.ipaddr
##            obj2.save()
##            obj2=police_drug_info_tb.objects.get(id=userid)
##            obj2.ipaddr=user_id.ipaddr
##            obj2.save()
##                role_type=register_tb.objects.all().values_list("role",flat=True).distinct()
            return render(request,"userhome.html",{"usernamee":user_id,"usr_id":userid,'imag':images,"txts":texts})
        elif count==1 and usertype=='admin':
            print("admin home")
            user_id=register_tb.objects.get(username=u,password=p)
            userid=user_id.id
            request.session['us_name']=userid
##            n=request.session['us_name']
            print ("user id:::::::::::::::::::::::::::_____________________",userid)
            user_dt=register_tb.objects.filter(role='user')
##            for i in user_data:
##                usernm=i.username
##                upass=i.password
##            print ("username:",usernm,"password:",upass)
##            images=image_tb.objects.filter(user_id=request.session['us_name'])
##            ob=register_tb.objects.filter(id=request.session['us_name'])
            dealer_drug=dealer_info_tb.objects.all().update(status="viewed")
            print("admin table status updated")
            
            dealer_drug=dealer_info_tb.objects.all()
            return HttpResponse("<script>alert('Welcome Admin');window.location.href=/adminhome/;</script>")
##            return render(request,"admin_home.html",{"user_dtt":user_dt,"drug_acc":dealer_drug})
        elif count==1 and usertype=='police':
             print("police station")
             user_id=register_tb.objects.get(username=u,password=p)
             userid=user_id.id
             request.session['us_name']=userid
             dealer_drug=police_drug_info_tb.objects.filter(status='viewed')
             print("already viewed dealers",dealer_drug.count())
             dealer_drug1=police_drug_info_tb.objects.filter(status=0)
             print("new viewed dealers",dealer_drug1.count())
##             dealer_drugs=police_drug_info_tb.objects.all().update(status="viewed")
             print("already viewed dealers",dealer_drug.count())
             print("new viewed dealers",dealer_drug1.count())
##             dealer_drug=police_drug_info_tb.objects.all()
             return render(request,"police_home.html",{"drug_acc":dealer_drug,"drug_acc_new":dealer_drug1})
        else:
            if count==0:
                usernm="user not exist"
                return HttpResponse("<script>alert('user not exist');window.location.href='registration.html';</script>")
            if count>1:
    ##            usernm="invalid user data, please check database"
                return HttpResponse("<script>alert('invalid user data, please check database');window.location.href='registration.html';</script>")
        print("............................................................................................................................................................")
    return HttpResponse("<script>window.location.href=/reg_page/;</script>")
def send_dealer_info_fn(request):
    print("send_dealer_info_fn")
    if request.method=="POST":
        police_viewed=[]
        admin_viewed=[]
        dealer_info_police=police_drug_info_tb.objects.all()#.update(status="viewed")
        print("dealer_info received police",dealer_info_police.count())
        for i in dealer_info_police:
            police_viewed.append(i.id)
        print("police have dealer info already",police_viewed)
        
        dealer_info=dealer_info_tb.objects.all()
        for i in dealer_info:
            admin_viewed.append(i.id)
            print("admin have dealer info already",admin_viewed)
            if i.id not in police_viewed:
                obj=police_drug_info_tb(
                        id=i.id,name=i.name,email=i.email,username=i.username,gender=i.gender,ipaddr=i.ipaddr
                        )
                obj.save()
        print("dealer_info received admin:",dealer_info.count)
####        ModelClass.objects.filter(name='bar').update(name="foo")
####        if dealer_info.count()!=0:
####            print("count..",dealer_info)
####            obj=police_drug_info_tb.objects.all().delete()
####            print("......deleted......")
##    ##    else:
##        if dealer_info.count()==0:#police table
##            dealer_drug=dealer_info_tb.objects.all()#admin table
##            if dealer_drug.count()>0:
##                for i in dealer_drug:
##                    obj=police_drug_info_tb(
##                        id=i.id,name=i.name,email=i.email,username=i.username,gender=i.gender,ipaddr=i.ipaddr
##                        )
##                    obj.save()
        print("information passed to police successfully")
        return HttpResponse("<script>alert('Information passed successfully');window.location.href=/adminhome/;</script>")
##        else:
##            dealer_drug=dealer_info_tb.objects.filter(status=0)#admin table
##            print("not sended dealers no: ",dealer_drug.count())
##            if dealer_drug.count()>0:
##                for i in dealer_drug:
##                    obj=police_drug_info_tb(
##                        id=i.id,name=i.name,email=i.email,username=i.username,gender=i.gender,ipaddr=i.ipaddr
##                        )
##                    obj.save()
##                print("information passed to police successfully")
##                return HttpResponse("<script>alert('Information passed successfully');window.location.href=/adminhome/;</script>")
        
            
    
def logout_fn(request):
    try:
        print ("logout_fn")
        if request.session.has_key('us_name'):
            print ("session=: deleting ",request.session['us_name'])
            user_dt=register_tb.objects.get(id=request.session['us_name'])
            if user_dt.role=='police':
                print("police logout")
                dealer_drugs=police_drug_info_tb.objects.all().update(status="viewed")
                print("status changed")
            print ("session=: deleting ",request.session['us_name'])
            del request.session['us_name']
            print ("session deleted")
            
            
            
        else:
##            return HttpResponse("plz login")
##            return render(request,"login.html",{})
            return HttpResponse("<script>alert('You logged out');window.location.href=/login_pg/;</script>")
    except Exception as e:
        print ("logout error",e)
    return HttpResponse("<script>alert('You logged out');window.location.href=/login_pg/;</script>")

##    return render(request,"login.html",{})
#-----------------------------------------------------View all users-------------------------------------------------
def all_user_fn(request):
    print ("all_user_fn")
    drug_dealer_acc_new=[]
    drug_dealer_acc_old=[]
    if request.session.has_key('us_name'):
        user_dt=register_tb.objects.filter(role='user')
        dealer_drug=dealer_info_tb.objects.all()
        if dealer_drug.count()!=0:
            for i in dealer_drug:
                drug_dealer_acc_old.append(i.id)
                print("drug_dealer_acc_old",drug_dealer_acc_old)
        for i in user_dt:
            print("i.id",i.id)
            imag_drug=image_tb.objects.filter(user_id=i.id,status='drug')
            text_drug=text_tb.objects.filter(user_id=i.id,status='drug')
            print("image drug:",imag_drug.count())
            print("text drug:",text_drug.count())
            if ((imag_drug.count()+text_drug.count())>5):
                print(i.name,"*******************")
                if i.id not in drug_dealer_acc_old:
                    drug_dealer_acc_new.append(i.id)
                    obj=dealer_info_tb(
                        id=i.id,name=i.name,email=i.email,username=i.username,gender=i.gender,ipaddr=i.ipaddr
                        )
                    obj.save()
            print("drug_dealer_acc_new",drug_dealer_acc_new)
        dealer_drug=dealer_info_tb.objects.all()
        print("........................dealer count...........",dealer_drug.count())
        return render(request,"admin_home.html",{"user_dtt":user_dt,"drug_acc":dealer_drug})
    return HttpResponse("<script>alert('Please Login');window.location.href='/login_pg/';</script>")

#-----------------------------------------------------View all users-------------------------------------------------

# import the necessary packages
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import argparse
import imutils
import cv2
from keras import backend as K
def test_img(img):
    K.clear_session()
    # load the image
    ##image = cv2.imread("281.jpg")
    ##image = cv2.imread("bb.jpg")
    image = cv2.imread("instagramapp\\static\\images\\"+img)
    print("IMAGE",image)
    ##image = cv2.imread("n7.jpg")
    orig = image.copy()

    # pre-process the image for classification
    image = cv2.resize(image, (100, 100))
    image = image.astype("float") / 255.0
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    # load the trained convolutional neural network
    print("[INFO] loading network...")
    
    model = load_model("instagramapp\\model")

    #classify the input image
    ##print("image[0]",image[0])
    (notdrug, drug) = model.predict(image)[0]
    # build the label
    print ("drug",drug)
    print ("notdrug",notdrug)
    #returning result drug or non drug
    label = "Drug" if drug > notdrug else "Not Drug"
    proba = drug if drug > notdrug else notdrug
    print ("label-----------",label)
    labels = "{}: {:.2f}%".format(label, proba * 100)
    K.clear_session()
    return label

def loadimg(request):
    iid=int(request.session['us_name'])
    usernm=register_tb.objects.get(id=iid)
    if request.method=="POST":
        print("username_________________________________",usernm)
        obj1=request.POST.get("uploadFromPC")
        print("obj1",obj1)
        obj=request.FILES["uploadFromPC"]
        print("image name-------------------------------------------------------",obj.name)
        if obj:
            fs = FileSystemStorage("instagramapp\\static\\images\\")
            nam1=random()
            nam2=str(nam1)
            nam=nam2[2:5] +obj.name
            nam=obj.name
            fs.save(nam,obj)
           
        ####    obj1=filetb.objects.get(userid=int(request.session["iid"])).update(filename=obj.name)
            
            print("uploaded")
            try:
                res=test_img(nam)
                print("..........................predicted result................",res)
                if res=="Drug":
                     obj1=image_tb(user_id=iid,image_nm=nam,status="drug")
                     obj1.save()
                     obj2=register_tb.objects.get(id=iid)
                     #updating the ipaddress
                     obj2.ipaddr=IPAddr
                     obj2.save()
                     print("address updated")
                     K.clear_session()
                else:
                    obj1=image_tb(user_id=iid,image_nm=nam,status="notdrug")
                    obj1.save()
                    K.clear_session()
                print(".......................predicted.....................")
                return HttpResponse("<script>alert('uploaded successfully');window.location.href=/userhome_pg/;</script>")
            except:
                return HttpResponse("<script>alert('Sorry unable to upload, Please upload an image file');window.location.href=/userhome_pg/;</script>")
    ##        return render(request,"home.html",{})
        else:
            return HttpResponse("Error")
    return render(request,"userhome.html",{"usernamee":usernm})
import datetime
import nltk
import pandas as pd
import numpy as np
import time
import re
import sys
import pickle
def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features

def get_words_in_sentences(sentences):
    all_words = []
    for (words, sentiment) in sentences:
        all_words.extend(words)
    return all_words
def test_post(com):
    if sys.version_info[0] == 3:
        xrange = range
    print ("com",com)
    print(type(com))
    if len(com)<=3:
        desicion='not drug'
    else:
        train = pd.read_csv("textdata.csv", header=0,delimiter=",", quoting=1, quotechar='"',encoding = "ISO-8859-1", engine='python')
        num_reviews = train["statements"].size
        print ("num_reviews",num_reviews)
        sentences = []

        for i in xrange(0, num_reviews):
            print(i,"ii.............",train["statements"][i])
            # Convert www.* or https?://* to URL
            sente = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', '', train["statements"][i])
            # Convert @username to AT_USER
            sente = re.sub('@[^\s]+', '', sente)
            # Remove additional white spaces
            sente = re.sub('[\s]+', ' ', sente)
            # Replace #word with word
            sente = re.sub(r'#([^\s]+)', r'\1', sente)
            # trim
            sente = sente.strip('\'"')
            words_filtereds = [e.lower() for e in sente.split() if len(e) >= 3]
            sentences.append((words_filtereds, train["Labels"][i]))
        print(".................... COMPLETED.................................")
        word_features = get_word_features(get_words_in_sentences(sentences))

        def extract_features(document):
            document_words = set(document)
            features = {}
            for word in word_features:
                features['contains(%s)' % word] = (word in document_words)
            return features

        sents = com
        desicion = ""
        attc = ""
        if len(sents) > 1:
            
                #every char except alphabets is replaced
                sente=re.sub('[^a-z\s]+',' ',sente,flags=re.IGNORECASE)
                # Convert to lower case
                # sente = sente_tests.lower()
                sente = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', '', com)
                sente = re.sub('@[^\s]+', '', sente)
                # Remove additional white spaces
                sente = re.sub('[\s]+', ' ', sente)
                # Replace #word with word
                sente = re.sub(r'#([^\s]+)', r'\1', sente)
                # trim
                sente = sente.strip('\'"')
                f = open("myclass.pickle", 'rb')
                classi = pickle.load(f)
                emot = classi.classify(extract_features(sente.split()))
                print (emot)
                desicion = emot
                dic = com + "=" + emot + "\n"

    desicion = desicion.strip()
    print ("..............................Desicion", desicion)
    return desicion

#------------------------------------------------------adding text post----------------------------------------------------------------------
def add_post(request):
    iid=int(request.session['us_name'])
    usernm=register_tb.objects.get(id=iid)
    if request.method=="POST":
        try:
            txxt=request.POST.get("post")
            txt=txxt#.decode()  
            if txt:
                print("in add_post txt",txt)
                result=test_post(txt)
                print("in add_post after res")
                if result=='drug':
                    obj1=text_tb(user_id=iid,text_post=txt,status="drug")
                    obj1.save()
                    obj2=register_tb.objects.get(id=usernm.id)
                    obj2.ipaddr=IPAddr
                    obj2.save()
                    print("address updated",usernm.id,IPAddr)
                    print ("added text....................................................",txt)
                else:
                    obj1=text_tb(user_id=iid,text_post=txt,status="notdrug")
                    obj1.save()
                    print ("added text....................................................",txt)                
    ##            return HttpResponse("<script>alert('Post added successfully');window.location.href='userhome.html';</script>")
                return HttpResponse("<script>alert('Post added successfully');window.location.href=/userhome_pg/;</script>")
        except:
            return HttpResponse("<script>alert('Sorry unable to upload, Please upload a text');window.location.href=/userhome_pg/;</script>")
        else:
            print("no text")
    ##        ob.save()
        
    return render(request,"userhome.html",{"usernamee":usernm})
def edit_profile(request):
    print("edit_profile")
    iid=int(request.session['us_name'])
    usernm=register_tb.objects.get(id=iid)
    print ("user name::::::::::::::",usernm.username)
    if request.method=="POST":
        print("in post function")
        name=request.POST.get("name")
        email=request.POST.get("email")
        uname=request.POST.get("username")
        paswd=request.POST.get("password")
        print ("name,email,uname,paswd",name,email,uname,paswd)
        u=name.replace(' ','.')
        print("uuuuuuu",u)
        obj_update=register_tb.objects.get(id=int(request.session['us_name']))
        obj_update.name=u.upper()
        obj_update.email=email
        obj_update.username=uname
        obj_update.password=paswd
        obj_update.save()
        return HttpResponse("<script>alert('Profile edited successfully');window.location.href=/userhome_pg/;</script>")
    return render(request,"userhome.html",{"usernamee":usernm})
