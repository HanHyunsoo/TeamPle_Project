from django.shortcuts import render, redirect
from django.contrib import auth
from .forms import SignUpForm, SignInForm
from .models import User


# Create your views here.

# 회원가입
def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        # 폼이 검증되면 로그인 되고 sign_up url로 넘어감(이 부분은 메인 화면으로 넘어가도록 수정할 예정)
        if form.is_valid():
            form.save()
            auth.login(request, User.objects.get(username=form.cleaned_data['username']))
            return redirect('account:sign_up')
        # 폼이 검증이 안되면 22번째 줄로 넘어가 에러메세지를 포함한 폼을 보내 템플릿을 렌더링함
    # request가 get이면 빈폼을 생성하고 22번째로 넘어가 템플릿 렌더링
    else:
        form = SignUpForm()

    return render(request, 'account/sign_up.html', {'form': form})


# 로그인
def sign_in(request):
    if request.method == "POST":
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # 폼이 검증되고 입력받은 아이디와 비밀번호가 일치하는 User모델을 user 변수에 저장
            user = auth.authenticate(username=username, password=password)

            # user가 존재하면 로그인을 하고 메인화면으로 넘어감(메인이 구현안되있어 로그인으로 넘어가게 수정함)
            if user:
                auth.login(request, user)
                return redirect('account:sign_in')
            # 만약 존재하지 않으면 form에 에러메세지를 추가하고 46번째 줄로넘어가 템플릿을 렌더링함
            form.add_error(None, '아이디 또는 비밀번호가 올바르지 않습니다.')
    # 방식이 get일때 빈폼을 생성하고 46번째 줄로넘어가 로그인 템플릿을 폼을 포함하여 렌더링한다
    else:
        form = SignInForm()

    return render(request, 'account/sign_in.html', {'form': form})


# 로그아웃
def sign_out(request):
    auth.logout(request)
    return redirect('account:sign_in')
