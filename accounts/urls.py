from django.contrib.auth import views as auth_view
from django.urls import path
from .views import *


urlpatterns = [
    path('login/', auth_view.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('register/', register, name='register'),
    path('myinfo/', Index.as_view(template_name='accounts/myinfo.html'), name='myinfo'),
    path('salesman/', Salseman_List.as_view(), name='salesman'),
    path('salesman/create', Sales_CreateView.as_view(), name='salesman_create'),
    path('salesman/update/<int:pk>/', Sales_UpdateView.as_view(), name='salesman_update'),
    path('salesman/delete/<int:pk>/', Sales_DeleteView.as_view(), name='salesman_delete'),
    path('', Index.as_view(), name='index'),



]