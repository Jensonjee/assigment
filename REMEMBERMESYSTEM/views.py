from unicodedata import name
from django.shortcuts import redirect, render
from .models import student,facultyreg,events,report
from .forms import studentform,facultyform,reportform
from django.contrib.auth import logout
from datetime import date
import datetime

from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def index(request):
    return render(request, 'index.html')
   
def stureg(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone_no=request.POST.get('phone_no')
        dob=request.POST.get('dob')
        admission_no=request.POST.get('admission_no')
        course=request.POST.get('course')
        batch=request.POST.get('batch')
        username=request.POST.get('username')
        password=request.POST.get('password')

        student(name=name,email=email,phone_no=phone_no,dob=dob,admission_no=admission_no,course=course,batch=batch,username=username,password=password).save()
    return render(request,'stureg.html')

def studentlogin(request):
    return render(request, 'studentlogin.html')

def studentlog(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        cr=student.objects.filter(username=username,password=password)
        if cr:
            dateofbirth=student.objects.all()
            for det in dateofbirth:
                dateofbirthsingle=det.dob
                usernamebirthday=det.username
                email=det.email
                today = datetime.date.today()

                if(dateofbirthsingle==today):

                    send_mail(
                    'Hi '+usernamebirthday+'' ,
                    'Happy Birthday',
                    'systemrememberme@gmail.com',
                    [email],
                    fail_silently=False
                )
            user_details=student.objects.get(username=username,password=password)
            id=user_details.id
            username=user_details.username
            email=user_details.email

            request.session['id']=id
            request.session['username']=username
            request.session['email']=email

            return redirect('studentwelcome')
        else:
            return render(request,'studentlogin.html')
    else:
        return render(request,'student.html')

def studentwelcome(request):
    id=request.session['id']
    username=request.session['username']
    email=request.session['email']
    return render(request,'studentwelcome.html',{'id':id,'username':username,'email':email})
        
def faculty(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone_no=request.POST.get('phone_no')
        dob=request.POST.get('dob')
        username=request.POST.get('username')
        password=request.POST.get('password')

        facultyreg(name=name,email=email,phone_no=phone_no,dob=dob,username=username,password=password).save()
    return render(request,'faculty.html')

def facultylogin(request):
    return render(request,'facultylogin.html')

def facultylog(request):
    if request.method=="POST":
        usernameinp=request.POST.get('username')
        password=request.POST.get('password')
        dob=request.POST.get('dob')

        cr=facultyreg.objects.filter(username=usernameinp,password=password,)
        if cr:
            dateofbirth=facultyreg.objects.all()
            for det in dateofbirth:
                dateofbirthsingle=det.dob
                usernamebirthday=det.username
                email=det.email
                today = datetime.date.today()
                print('date of birth single',dateofbirthsingle)
                print('today',today)

                if(dateofbirthsingle==today):
                    print('yes birth day')
                    send_mail(
                    'Hi '+usernamebirthday+'' ,
                    'Happy Birthday',
                    'systemrememberme@gmail.com',
                    [email],
                    fail_silently=False
                )
                #     print(usernamebirthday,'birthday')
                else:
                    print('no')

            user_details=facultyreg.objects.get(username=usernameinp,password=password)
            id=user_details.id
            username=user_details.username
            email=user_details.email
            

            request.session['id']=id
            request.session['username']=username
            request.session['email']=email


            return redirect('welcome')
        else:
            return render(request,'facultylogin.html')
    else:
        return render(request,'faculty.html')

def welcome(request):
    id=request.session['id']
    username=request.session['username']
    email=request.session['email']
    

    return render(request,'welcome.html',{'id':id,'username':username,'email':email})

def views(request):
     if request.method=='POST':
       choose_date1 = request.POST.get('date')
       ce=events.objects.filter(choose_date=choose_date1)
       if ce:
        return render(request,"views.html",{'ce':ce})
        
     return render(request,"views.html")

def eventview(request):
    print(request)
    id=request.session['id']
    choose_date=request.session['choose_date']
    eventsname=request.session['eventsname']

    # cr=events.objects.all().filter(choose_date='')

    
    return render(request,'eventview.html',{'id':id,'eventsname':eventsname,'choose_date':choose_date})

def update(request,pk):
    cr=student.objects.get(id=pk)
    form=studentform(instance=cr)
    if request.method=="POST":
        form=studentform(request.POST,instance=cr)
        if form.is_valid:
            form.save()
            return redirect("welcome")
    return render(request,"update.html",{'form':form})

def logoutuser(request):
    logout(request)
    return redirect('index')

def reports(request):
    if request.method=="POST":
        event=request.POST.get('event')

        report(event=event).save()
    return render(request, 'reports.html')

def inbox(request):
     today = date.today()
     print("Today's date:", today)
     cr=events.objects.filter(choose_date=today)
     sr=events.objects.filter(eventsname='birthday',choose_date=today)
     print("choose_date",cr)
     print("birthday",cr)
     if cr:

       return render(request,"inbox.html",{'cr':cr})
     if sr:
        return render(request,"birthday.html",{'sr':sr})
     return render(request,'inbox.html')

def birthday(request):
    return render(request,'birthday.html')


def file(request):
    form = reportform()
    if request.method =="POST":
        form = reportform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    return render(request,"file.html",{'form':form})

# def file(request):
#     if request.method=="POST":
#         event=request.POST.get('event')
#         reports=request.POST.get('reports')

#         report(event=event,reports=reports).save()
#     return render(request,'file.html')