
from django.urls import path
from .views import RegisterUser,User_Login,User_logout


urlpatterns = [
    path('register/', RegisterUser, name='register'),
    path('login/', User_Login, name='login'),
    path('logout/', User_logout, name='logout'),
]