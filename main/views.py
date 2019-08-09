from django.shortcuts import render
from account.forms import SignInForm, SignUpForm

# Create your views here.
def home(request):#메인페이지를 띄웁니다.
    form = SignInForm()
    up_form = SignUpForm()
    return render(request, 'layout.html', {'form': form, 'up_form': up_form})
