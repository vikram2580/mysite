from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse,redirect
from datetime import datetime
from myapp.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,  login, logout

# Create your views here.
def index(request):
     return render (request,'index.html')
    #return HttpResponse("hello world")

def handleSignup(request):
    if request.method =='POST':
        # Get the post parameters
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

         # check for errorneous input
        if len(username)<10:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('home')
        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('home')
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your account has successfully created")
        return redirect('/')


    else:
        return HttpResponse("404 not allowed")

def handeLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")

    return HttpResponse("404- Not found")
   

    return HttpResponse("login")

def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')




def about(request):
    return render (request,'about.html')


def services(request):
    return render (request,'services.html')



def contact(request):
    if request.method=="POST":
        name = request.POST.get('name')

        email = request.POST.get('email')

        phone = request.POST.get('phone')

        desc = request.POST.get('desc')
        contact= Contact (name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Infromation has been sent!') 

    return render (request,'contact.html')


