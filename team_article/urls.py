from django.urls import path
from . import views

app_name = 'team_article'
urlpatterns = [
    path('<int:team_pk>/<int:user_pk>/workspace/', views.workspace, name='workspace'),
    path('<int:team_pk>/<int:user_pk>/workspace/url', views.articleurl, name='articleurl'),
    path('<int:team_pk>/<int:user_pk>/workspace/file', views.articlefile, name='articlefile'),
]