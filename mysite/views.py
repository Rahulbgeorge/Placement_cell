from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from . import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from . import models

from datetime import datetime

from django.forms import DateField
from datetime import datetime

# Create your views here
def login_page(request):
    content = {}
    if request.method == 'POST':
        logform = forms.login_form(request.POST)
        content = {'logform': logform}

        if logform.is_valid():
            user = authenticate(request, username=logform.cleaned_data['username'], password=logform.cleaned_data['password'])
            print("reached authentication")
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/upload/')
                content['log_response'] = 'Valid password'

            else:
                content['log_response'] = 'Invalid password'
                content['login'] = forms.login_form()
    else:
        content['login'] = forms.login_form()

    return render(request, 'registration/login.html', content)



def home(request):
    return HttpResponse("<h1>This page is loading i guess</h1>")



def logout_page(request):
    logout(request)
    return HttpResponse("<h1 style='text-align:center;'>Successfully logged-out</h1>")

def home(request):
    content={}
    notilist=[]
    query=models.Notifications.objects.all().order_by("-Date")[:5]
    for i in query:
        if(i.picture==''):
            i.picture='noimage.png'
        notilist.append(i)
    content['notifications']=notilist

    return render(request,'notifications.html',content)



#to upload files from user
def upload_file(request):
    content = {}
    a = models.Notifications.objects.all().order_by("-Date")

    if(request.user.is_authenticated()):
        if request.method == 'POST':
            form = forms.notification_form(request.POST, request.FILES)
            if form.is_valid():

                if 'file' in list(request.FILES.keys()):
                    instance = models.Notifications(content=form.cleaned_data['content'],topic=form.cleaned_data['topic'],picture=request.FILES['file'],Date=datetime.now())
                    instance.save()
                    return render(request, 'upload.html', {'log_response': "file uploaded succcessfully"})

                else:
                    instance = models.Notifications(content=form.cleaned_data['content'], topic=form.cleaned_data['topic'],picture=None, Date=datetime.now())
                    instance.save()
                    content['log_response']='File uploaded successfully!!'
                    return HttpResponseRedirect("/upload/")


            else:
                for i in a:
                    print("looping")
                    if request.POST.get("val_"+str(i.id)):
                        print("cautht you "+i.topic)
                        models.Notifications.objects.filter(id=i.id).delete()
                        return HttpResponseRedirect("/upload/")
                        print("Response achieved")



        form = forms.notification_form()
        content['form']=form
    else:
        return HttpResponse("<h1 style='text-align:center;'>NO ADMIN ACCESS!!</h1>")


    data = []
    for i in a:
        if (i.picture == ''):
            i.picture = 'noimage.png'
        data.append(i)
    content['data'] = data
    return render(request, 'upload.html', content)

def alumni_page(request):
    return render(request,'alumni_page.html')