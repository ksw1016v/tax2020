from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from datetime import datetime
from .models import *
from django.db.models import Q
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



#가망고객의 리스트보기 admin 일때는 전체리스트, 개인일때는 각자의 리스트만 확인하고 회사이름, 영업자이름 내부외부 등으로 검색가능
class CustomerlistView(LoginRequiredMixin,ListView):
    model = Customer
    paginate_by = 30
    ordering = ['company']

    def get_queryset(self, *args, **kwargs):
        queryset_list = Customer.objects.select_related('sales').all()
        query = self.request.GET.get("q")
        if query:
               queryset_list = queryset_list.filter(
                   Q(company__icontains=query) |
                   Q(sales__name__icontains=query)
               ).distinct()
        else:
               queryset_list = queryset_list.all()
        return queryset_list


#가망고객추가 : 로그인한 사람을 영업자로 등록
class Customer_CreateView(LoginRequiredMixin,CreateView):
    model = Customer
    form_class =CustomerCreateForm
    success_url = reverse_lazy('customerlist')
    template_name_suffix = '_create'



class Customer_UpdateView(LoginRequiredMixin, UpdateView):
    model = Customer
    form_class = Customer_UpaateForm
    success_url = reverse_lazy('customerlist')
    template_name_suffix = '_update'



class Customer_DeleteView(LoginRequiredMixin,DeleteView):
    model = Customer
    success_url = reverse_lazy('customerlist')