from django.shortcuts import render, redirect
from .forms import SignUpForm
from .models import User


# Create your views here.
def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account:sign_up')
    else:
        form = SignUpForm()
        print(form)

    return render(request, 'account/sign_up.html', {'form': form})

