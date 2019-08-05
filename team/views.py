from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.utils import timezone
from .models import Team, TeamMember
from account.models import User
from .forms import TeamForm, AddForm

# Create your views here.

def detail_team(request, team_id, user_id):
   user = get_object_or_404(User, pk=user_id)
   details = get_object_or_404(Team, pk=team_id)
   team_member = TeamMember.objects.filter(team=details)
   return render(request, 'team/detail_team.html', {'details': details,'user':user, 'team_member':team_member})


def create_team(request, user_id):
   # user = get_object_or_404(User, pk=user_id)
   user = request.user
   if request.method == 'POST':
         form = TeamForm(request.POST)
         if form.is_valid():
            team = form.save()
            TeamMember.objects.create(team=team, user=user)
            # team.members.add(user)
            team.team_leader.add(user)
            team.created_date = timezone.now()
            team.save()
            return redirect('team:detail_team', team.id, user.id)
   else:
         teamform = TeamForm()
         return render(request, 'team/create_team.html', {'teamform': teamform})


def add_member(request, team_id, user_id):
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
                  return redirect('team:detail_team', team_id, user_id)
         
         # elif TeamMember.objects.filter(team=team1, user=member.user):
         #    return HttpResponse('해당사용자가 팀에 존재합니다!')
         else:
            return HttpResponse('해당 사용자가 존재하지 않습니다!')

   else:
      form = AddForm()
      return render(request, 'team/add_member.html', {'form':form})      

def expulsion_member(request, team_id, user_id): #어느 팀에서 몇번 째 유저를 삭제할지.
   login_user = request.user
   team = get_object_or_404(Team, pk=team_id)  #어느 팀 객체인지 가져오고
   user = get_object_or_404(User, pk=user_id)  #어느 유저 객체인지 가져온 다음에
   delete_member = TeamMember.objects.filter(team=team, user=user)  #외래키 설정 되어있는 team과 user 에 각각을 매칭 시켜주기
   delete_member.delete()
   return redirect('team:detail_team', team_id, login_user.id)
    
# def team_delete(request, team_id, user_id):  #team_id = 제거하려는 팀 id, user_id = 팀 리더의 값을 알아내기 위해.
#    team_main = get_object_or_404(Team, pk=team_id)
#    user_leader = get_object_or_404(User, pk=user_id)
#    team_main = Team.objects.filter(team_leader=user_leader)
#    team_main.delete()
#    return redirect('account:user_home', user_id)
   
#    # else:
#    #    return HttpResponse('해당 리더가 아닙니다!') 

def leave_team(request, team_id, user_id):
   user = get_object_or_404(User, pk=user_id)
   team = get_object_or_404(Team, pk=team_id)
   if TeamMember.objects.filter(team=team):  #TeamMember 안에 객체가 있으면 해당 유저를 팀에서 나가고
      leave = TeamMember.objects.filter(team=team, user=user)
      leave.delete()      
      return redirect('account:user_home', user_id)
   
   else:
      team = get_object_or_404(Team, pk=team_id)
      team.delete()
      return 