from django.urls import path
from . import views

app_name = 'mail'
urlpatterns = [
    path('mypage/<int:user_id>', views.mypage, name='mypage'),
    path('send_mail/<int:from_id>/', views.send_mail, name='send_mail'),
]