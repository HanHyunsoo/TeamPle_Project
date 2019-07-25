from django import forms
from .models import Team, TeamMember
from team_article.models import Article
class TeamForm(forms.ModelForm):
    class Meta:
            
        model = Team
        fields = ['team_name', 'introduce']