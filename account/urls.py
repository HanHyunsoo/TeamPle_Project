from django.urls import path
from . import views


app_name = 'account'
urlpatterns = [
    path('sign-up/', views.sign_up, name='sign_up'),
    path('sign-in/', views.sign_in, name='sign_in'),
    path('sign-out/', views.sign_out, name='sign_out'),
    path('user-home/<int:user_pk>', views.user_home, name='user_home'),
    path('user_imfo/<int:user_pk>', views.user_info, name='user_imfo'),
]