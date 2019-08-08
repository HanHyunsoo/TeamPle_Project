from django import forms
from account.models import User
from .models import Team, TeamMember
# from team_article.models import Article

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['team_name', 'introduce']

# class AddForm(forms.Form):
#     username = forms.CharField(max_length=20)

class AddForm(forms.ModelForm):
    username = forms.CharField(max_length=20)
    class Meta:
        model = TeamMember
        fields = ['username']
             
class EditForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['team_name', 'introduce', 'team_photo_url']   
# class AddForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username']