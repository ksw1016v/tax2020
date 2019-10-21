from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from django.urls import reverse_lazy
from django.db.models import Q


# Create your views here.


#회원가입
def register(request):
    if request.method =='POST':
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return redirect('login')
    else:
        user_form = RegisterForm()

    return render(request, 'accounts/register.html', {'form':user_form})




#index 로그인 후 나타나는 메인페이지
class myinfo_List(LoginRequiredMixin,ListView):
    model = Account
    template_name = 'accounts/index.html'


    def get_queryset(self, *args, **kwargs):
        queryset_list = Account.objects.filter(username=self.request.user.username)
        return queryset_list

class Index(LoginRequiredMixin,ListView):
    model = Account
    template_name = 'accounts/index.html'


    def get_queryset(self, *args, **kwargs):
        queryset_list = Account.objects.filter(username=self.request.user.username)
        return queryset_list


class Salseman_List(LoginRequiredMixin,ListView):
    model = Sales

    def get_queryset(self, *args, **kwargs):
        queryset_list = Sales.objects.all()
        query = self.request.GET.get("q")
        if query:
               queryset_list = queryset_list.filter(
                   Q(name__icontains=query) |
                   Q(team__icontains=query)
               ).distinct()
        else:
               queryset_list = queryset_list.all()
        return queryset_list




class Sales_CreateView(LoginRequiredMixin,CreateView):
    model = Sales
    form_class =Sales_CreateForm
    success_url = reverse_lazy('salesman')
    template_name_suffix = '_create'



class Sales_UpdateView(LoginRequiredMixin,UpdateView):
    model = Sales
    form_class =Sales_UpaateForm
    success_url = reverse_lazy('salesman')
    template_name_suffix = '_create'



class Sales_DeleteView(LoginRequiredMixin,DeleteView):
    model = Sales
    success_url = reverse_lazy('salesman')