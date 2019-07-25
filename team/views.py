from django.shortcuts import render,redirect
from django.utils import timezone
from .models import Team, TeamMember
from account.models import User
from .forms import TeamForm
# Create your views here.

def user_list(request):
    users = User.objects
    return render(request, 'team/user_list.html', {'users':users})

def team_page(request):
    teams = Team.objects
    return render(request,'team/team_page.html',{'teams':teams})


def teamform(request, team=None):       
    if request.method == 'POST':
        form = TeamForm(request.POST, instance=team)
        if form.is_valid():
            team = form.save(commit=False)
            team.created_date = timezone.now()
            team.save()
            return redirect('team_page')
    else:
        form = TeamForm(instance=team)
        return render(request, 'team/create_team.html', {'form': form})

# def member_list(request):
#     team = Team.objects.all()

    
