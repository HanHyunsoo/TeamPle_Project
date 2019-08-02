from django.shortcuts import render

# Create your views here.
def home(request):#메인페이지를 띄웁니다.
    return render(request, 'main.html')