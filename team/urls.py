from django.urls import path
from . import views
app_name = 'team'
urlpatterns = [
    path('create_team/<int:user_id>/',views.create_team, name='create_team'),
    path('team_page/', views.team_page, name='team_page'),
    path('<int:team_id>/<int:user_id>/', views.detail_team, name="detail_team"),
    path('<int:team_id>', views.add_member,name="add_member"),
    path('<int:team_id>', views.correct_team, name="correct_team"),
]