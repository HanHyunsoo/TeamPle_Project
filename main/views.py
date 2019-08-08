from django.shortcuts import render
from account.forms import SignInForm, SignUpForm

# Create your views here.
def home1(request):#메인페이지를 띄웁니다.
    signinform = SignInForm()
    signupform = SignUpForm()
    return render(request, 'main/main.html', {'signinform':signinform, 'signupform':signupform})

