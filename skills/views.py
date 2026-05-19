from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password,check_password
from django.http import HttpResponse
from skills .models import signupm ,loginp
# from django.contrib.auth.hashers import make_password ,check_password


def home(req):
    return render(req,'skill_home.html')


def about(req):
    return render(req,'skill_about.html')



def service(req):
    return render(req,'skill_service.html')


def login(req):
       if req.method == 'POST':
        email = req.POST.get('email')
        password = req.POST.get('password')

        user = signupm.objects.filter(email=email).first()

        if user and check_password(password, user.password):
            return redirect('home')   # ✅ yahi tumko chahiye
        else:
            return HttpResponse('Invalid email or password')

       return render(req, 'skill_login.html')


def signup(req):
    if req.method == 'POST':
        username = req.POST.get('username')
        email = req.POST.get('email')
        mobile_no = req.POST.get('mobile_no')
        password = req.POST.get('password')

        # password hash karo
        hashed_password = make_password(password)

        signupm.objects.create(
            username=username,
            email=email,
            mobile_No=mobile_no,
            password=hashed_password
        )

        return redirect('login')

    return render(req, 'skill_signup.html')

# Create your views here.
