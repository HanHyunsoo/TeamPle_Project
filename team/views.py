from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.utils import timezone
from .models import Team, TeamMember
from account.models import User
from .forms import TeamForm, AddForm, EditForm

# Create your views here.

def team_page(request):
   teams = Team.objects
   return render(request, 'team/team_page.html', {'teams': teams})


def detail_team(request, team_id, user_id):
   user = get_object_or_404(User, pk=user_id)
   details = get_object_or_404(Team, pk=team_id)
   return render(request, 'team/detail_team.html', {'details': details,'user':user})


def create_team(request, user_id):
   # user = get_object_or_404(User, pk=user_id)
   user = User.objects.get(pk=user_id)
   if request.method == 'POST':
         form = TeamForm(request.POST)
         if form.is_valid():
            team = form.save()
            TeamMember.objects.create(team=team, user=user)
            # team.members.add(user)
            team.team_leader = user
            team.created_date = timezone.now()
            team.save()
            return redirect('team:team_page')
   else:
         form = TeamForm()
         return render(request, 'team/create_team.html', {'form': form})


def add_member(request, team_id, tm=None):
   team1 = get_object_or_404(Team, pk=team_id)
   if request.method == 'POST':
      form = AddForm(request.POST)
      if form.is_valid():
         member = form.save(commit=False)
         member.team = team1 #팀에대한 정보를 가져와 TeamMember의 team 에다가 저장을 하고.
         if User.objects.filter(username=form.cleaned_data['username']):
               member.user = User.objects.get(username=form.cleaned_data['username']) #해당유저에 대한 데이터를 가져오고
               if TeamMember.objects.filter(team=team1, user=member.user): #해당 팀에 user가 이미 존재해 있는 경우
                  return HttpResponse('해당사용자가 팀에 존재합니다!')
            
               else: # 해당 팀에 user가 존재하지 않는다면
                  tm = TeamMember(team=team1, user=member.user) 
                  tm.save()
                  return redirect('team:detail_team', team_id, tm.user.id)
         
         # elif TeamMember.objects.filter(team=team1, user=member.user):
         #    return HttpResponse('해당사용자가 팀에 존재합니다!')
         else:
            return HttpResponse('해당 사용자가 존재하지 않습니다!')

   else:
      form = AddForm()
      return render(request, 'team/add_member.html', {'form':form})


def correct_team(request, team_id):
   team_correct = get_object_or_404(Team, pk = team_id)
   if request.method == "POST":
      form = EditForm(data = request.POST, instance=request.team_correct)
      if form.is_valid():
         team_correct = form.save()
         return redirect('team/correct_team', team_id)
   else:
      form = EditForm(instance = request.team_correct)
      return redirect('team/correct_team', team_id)
    
      
   



    
