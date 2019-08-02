from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from .models import Mail
from account.models import User
from .forms import MailForm
from django.utils import timezone
# Create your views here.

def send_mail(request, from_id):
    from_user = get_object_or_404(User, pk=from_id)
    if request.method == 'POST':
        form = MailForm(request.POST)
        if form.is_valid():
            mail = form.save(commit=False)
            mail.from_user = from_user
            if User.objects.filter(username=form.cleaned_data['username']):
                mail.to_user = User.objects.get(username=form.cleaned_data['username'])
                mail.created_data = timezone.now()
                mail.modified_data = timezone.now()
                mail.save()
                return redirect('account:sign_in')
            else:
                return HttpResponse('사용자가 없습니다.')
    else:
        form = MailForm()
        return render(request, 'mail/send_mail.html', {'form': form})

def mypage(request, user_id):
    mails = get_object_or_404(User, pk=user_id)
    return render(request, 'mail/mypage.html', {'mails': mails})

# def send_mail(request):
#     if request.method == "POST":

#     else:
#         form = MailForm()
#         return render(request, 'mail/send_mail.html', {'form': form})