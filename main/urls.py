from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('home/', views.home1, name='home')
]