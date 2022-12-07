from django.shortcuts import render,redirect

from .models import new_user
from hashlib import sha256

# Create your views here.

def register(request):
    
    if request.method == 'POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        
        
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        password=sha256(pass2.encode()).hexdigest()
        phone=request.POST.get('phone')
        place=request.POST.get('place')
        new_user(username=username,email=email,password=password,phone=phone,place=place).save()

    return render(request,'index.html')


def login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        password2=sha256(password.encode()).hexdigest()
        user=new_user.objects.filter(username=username,password=password2)
        if user:
            user_details=new_user.objects.get(username=username,password=password2)
            id=user_details.id
            username_name=user_details.username
            place=user_details.place
            phone=user_details.phone
            request.session['id']=id
            request.session['username']=username_name
            request.session['place']=place
            request.session['phone']=phone

            return redirect('home')
        else:
            return redirect('login')
    return render(request,'login.html')


def home(request):
    id=request.session['id']
    username=request.session['username']
    place=request.session['place']
    phone=request.session['phone']
    return render(request,'home.html',{'id':id,'name':username,'place':place,'phone':phone})
