from django.shortcuts import render
from . models import Employe,leave,complaint
import smtplib
import random

# Create your views here.

def index(request):
    return render (request,'index.html')

def home(request):
    return render (request,'home.html')

def register(request):
    if request.method =='POST':
        first_name=request.POST.get('f_name')
        last_name=request.POST.get('l_name')
        address=request.POST.get('address')
        gender=request.POST.get('gender')
        state=request.POST.get('state')
        city=request.POST.get('city')
        birth=request.POST.get('dob')
        designation=request.POST.get('designation')
        number=random.randint(10000,1000000)
        password='employee' +str(number)
        email=request.POST.get('email')

        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("nefsal003@gmail.com", "htxalvzrrkxupspv")
    
        Employe(first_name=first_name,last_name=last_name,address=address,gender=gender,email=email,state=state,city=city,birth=birth,designation=designation,password=password).save()
       
       
        message = f"Congrates!!!your registration has been completed successfully {password}"
        s.sendmail("nefsal003@gmail.com", email, message)
        s.quit()
        return render(request,'login.html')
    else:
        return render(request,'register.html')  
    


def login(request):
    if request.method=='POST':
        pas=request.POST.get('password')
        mail=request.POST.get('email')
        cr = Employe.objects.filter(password=pas,email=mail)

        if cr:
          details = Employe.objects.get(password=pas,email=mail)
          firstname=details.first_name
          mail=details.email
          
          request.session['first_name']=firstname
          request.session['email']=mail

          return render (request,'home.html',{'p':firstname})
         
    else:
     return render(request,'login.html')
    
    
def myleaves(request):
    user=request.session['first_name']
    data=leave.objects.filter(name=user)
    return render(request,'view_leave.html',{'data':data})
    
  
def leaveform(request):
    if request.method=='POST':
        name=request.POST.get('name')
        date=request.POST.get('date')
        type=request.POST.get('type')
        reason=request.POST.get('reason')
        status='waiting'
        leave(name= name,date=date,type=type,reason=reason,status=status).save()
        return render(request,'confirm.html')
    else:
        
        user=request.session['first_name']
        return render (request,'leaveform.html',{'name':user})
    
def mycomplaint(request):
    if request.method=='POST':
        name=request.POST.get('name')
        date=request.POST.get('date')
        designation=request.POST.get('job')
        reason=request.POST.get('reason')
        complaint(name=name,date=date,designation=designation,reason=reason).save()
        return render(request,'index.html')
    else:
     return render(request,'complaint.html')
    

   
# def myleaves(request):
     
#     variableuser=request.session['first_name']
#     cr=leave.objects.get(name=variableuser)

#     name=cr.name
#     date=cr.date
#     type=cr.type
#     reason=cr.reason 

#     context={'name':name,
#              'date':date,
#              'type':type,
#              'reason':reason}

#     return render(request,'view_leave.html',context) 