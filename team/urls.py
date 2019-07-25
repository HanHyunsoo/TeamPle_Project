from django.urls import path
from . import views
app_name = 'team'
urlpatterns = [
    path('create_team/',views.teamform, name='create_team'),
    path('team_page/', views.team_page, name='team_page'),
    path('user_list/', views.user_list, name='user_list'),
]