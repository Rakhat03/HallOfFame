from django.urls import path
from .views import *
from django.contrib import auth
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    path('dashboard', dashboard, name='dashboard'),
    #Auth
    path('signup', SignUp.as_view(), name='signup'),
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    #Hall
    path('halloffame/create', CreateHall.as_view(), name = 'create_hall'),
    path('halloffame/<int:pk>', DetailHall.as_view(), name = 'detail_hall'),
    path('halloffame/<int:pk>/update', UpdateHall.as_view(), name = 'update_hall'),
    path('halloffame/<int:pk>/delete', DeleteHall.as_view(), name = 'delete_hall'),
    
]