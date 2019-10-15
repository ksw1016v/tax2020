from django.urls import path
from .views import *

urlpatterns = [


    path('supportslist/', WorklistView.as_view(), name='supportslist'),
    path('supportslist/create/', Work_CreateView.as_view(), name='supports_create'),
    path('supportslist/update/<int:pk>/', Work_UpdateView.as_view(), name='supports_update'),

    path('work_add_list/', Customer_work_Add_ListView.as_view(template_name='supports/work_add_list.html'), name='work_add_list'),
    path('work_add_list/create/<int:pk>/', Work_add_CreateView.as_view(), name='work_add_list_create'),
    path('working_list/', Working_listView.as_view(), name='working_list'),
    path('working_list/update/<int:pk>/', Working_UpdateView.as_view(), name='working_updatet'),

    path('working_result_list/', Working_result_listView.as_view(template_name='supports/working_result_list.html'), name='working_result_list'),


    path('result_list/update/<int:pk>/', Result_UpdateView.as_view(), name='result_update'),
    path('result_list/create/<int:pk>/', Result_CreateView.as_view(), name='result_create'),
    path('result_list/', Result_listView.as_view(), name='result_list'),


    path('result_pay_list/', Result_pay_listView.as_view(template_name='supports/result_pay_list.html'), name='result_pay_list'),
    path('result_pay_list/update/<int:pk>/', Result_pay_UpdateView.as_view(template_name='supports/result_pay_update.html'), name='result_pay_list_update'),

    path('result_pay_dashborad_list/', Result_pay_dashboradlistView.as_view(template_name='supports/result_pay_dashborad_list.html'), name='result_pay_dashborad_list'),
    path('Result_nopay_listView/', Result_nopay_listView.as_view(template_name='supports/result_nopay_list.html'), name='result_nopay_list'),
    path('dashborad/', Dashborad_listView.as_view(template_name='supports/dashborad_list.html'), name='dashborad'),
    path('dashborad/working_list/', Working_total_listView.as_view(template_name='supports/dashborad_working_list_total.html'), name='dashborad_working_list_total'),
    path('dashborad/total_amount/', Dashborad_amountlistView.as_view(template_name='supports/dashborad_total_amount.html'), name='dashborad_total_amount'),
    path('dashborad/total_pay/', Dashborad_paylistView.as_view(template_name='supports/dashborad_total_pay.html'), name='dashborad_total_pay'),
    path('dashborad/total_fee/', Dashborad_feelistView.as_view(template_name='supports/dashborad_total_fee.html'), name='dashborad_total_fee'),
    path('dashborad/sales_total/<int:pk>/', Dashborad_sales_totallistView.as_view(template_name='supports/sales_total.html'), name='sales_total'),




]