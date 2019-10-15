from django.urls import path
from .views import *

urlpatterns = [

    path('customerlist/', CustomerlistView.as_view(), name='customerlist'),
    path('customerlist/create/', Customer_CreateView.as_view(), name='customer_create'),
    path('customerlist/update/<int:pk>/', Customer_UpdateView.as_view(), name='customer_update'),

]