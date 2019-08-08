from django.urls import path
from . import views


app_name = 'account'
urlpatterns = [
    path('sign_up/', views.sign_up, name='sign_up'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('sign_out/', views.sign_out, name='sign_out'),
    path('user_home/<int:user_pk>', views.user_home, name='user_home'),
    path('user_info/<int:user_pk>', views.user_info, name='user_imfo'),
    path('schedule/', views.set_schedule, name='set_schedule'),
]