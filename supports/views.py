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
from customers import models as customers_models
from accounts import models as accounts_models
from django.db.models import Count, Sum, Avg






class WorklistView(LoginRequiredMixin,ListView):
    model = Work
    paginate_by = 30
    ordering = ['work_name']

    def get_queryset(self, *args, **kwargs):
        queryset_list = Work.objects.all()
        query = self.request.GET.get("q")
        if query:
               queryset_list = queryset_list.filter(
                   Q(work_name__icontains=query)
               ).distinct()
        else:
               queryset_list = queryset_list.all()
        return queryset_list





#가망고객추가 : 로그인한 사람을 영업자로 등록
class Work_CreateView(LoginRequiredMixin,CreateView):
    model = Work
    form_class =WorkCreateForm
    success_url = reverse_lazy('supportslist')
    template_name_suffix = '_create'

class Work_UpdateView(LoginRequiredMixin,UpdateView):
    model = Work
    form_class =WorkUpdateForm
    success_url = reverse_lazy('supportslist')
    template_name_suffix = '_create'


class Customer_work_Add_ListView(LoginRequiredMixin,ListView):
    model = customers_models.Customer
    paginate_by = 30
    ordering = ['company']

    def get_queryset(self, *args, **kwargs):
        queryset_list = customers_models.Customer.objects.select_related().all()
        query = self.request.GET.get("q")
        if query:
               queryset_list = queryset_list.filter(
                   Q(company__icontains=query) |
                   Q(sales__name__icontains=query)
               ).distinct()
        else:
               queryset_list = queryset_list.all()
        return queryset_list





class Work_add_CreateView(LoginRequiredMixin,CreateView):
    model = Working
    form_class = Work_add_CreateForm
    success_url = reverse_lazy('work_add_list')
    template_name_suffix = '_create'

    def form_valid(self, form):
        form.instance.company = customers_models.Customer.objects.get(pk=self.kwargs.get('pk'))
        return super(Work_add_CreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['customers'] = customers_models.Customer.objects.filter(pk=self.kwargs['pk'])
        return context




class Working_listView(LoginRequiredMixin,ListView):
    model = Working
    fields = '__all__'
    paginate_by = 30
    ordering = ['work_name']

    def get_queryset(self, *args, **kwargs):
        queryset_list = Working.objects.select_related('company').filter(~Q(ing="계약완료"))

        query = self.request.GET.get("q")
        if query:
               queryset_list = queryset_list.filter(
                   Q(company__company__icontains=query) |
                   Q(company__sales__name__icontains=query) |
                   Q(work_name__work_name__icontains=query) |
                   Q(ing__icontains=query)
               ).distinct()
        elif self.request.GET.get('start_date') and self.request.GET.get('end_date'):
                start_date1 = self.request.GET.get('start_date')
                start_date = datetime.datetime.strptime(start_date1, '%Y-%m-%d')
                end_date1 = self.request.GET.get('end_date')
                end_date = datetime.datetime.strptime(end_date1, '%Y-%m-%d')
                term = (start_date, end_date + datetime.timedelta(days=1))
                queryset_list = Working.objects.filter(created__range=term)
        else:
               queryset_list = queryset_list.all()
        return queryset_list



class Working_result_listView(LoginRequiredMixin,ListView):
    model = Working
    fields = '__all__'
    paginate_by = 30
    ordering = ['work_name']

    def get_queryset(self, *args, **kwargs):
        queryset_list = Working.objects.select_related('work_name').filter(Q(ing= "계약완료"))
        query = self.request.GET.get("q")
        if query:
               queryset_list = queryset_list.filter(
                   Q(company__company__icontains=query) |
                   Q(company__sales__name__icontains=query) |
                   Q(work_name__work_name__icontains=query) |
                   Q(ing__icontains=query)
               ).distinct()
        elif self.request.GET.get('start_date') and self.request.GET.get('end_date'):
                start_date1 = self.request.GET.get('start_date')
                start_date = datetime.datetime.strptime(start_date1, '%Y-%m-%d')
                end_date1 = self.request.GET.get('end_date')
                end_date = datetime.datetime.strptime(end_date1, '%Y-%m-%d')
                term = (start_date, end_date + datetime.timedelta(days=1))
                queryset_list = Working.objects.filter(updated__range=term)
        else:
               queryset_list = queryset_list.all()
        return queryset_list




class Working_UpdateView(LoginRequiredMixin, UpdateView):
    model = Working
    form_class = Working_upaate_CreateForm
    success_url = reverse_lazy('working_list')
    template_name_suffix = '_update'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['workings'] = Working.objects.filter(pk=self.kwargs['pk'])
        return context




class Result_listView(LoginRequiredMixin,ListView):
    model = Result
    fields = '__all__'
    paginate_by = 30
    ordering = ['_work_date']

    def get_queryset(self, *args, **kwargs):
        queryset_list = Result.objects.select_related('work_name').all()
        query = self.request.GET.get("q")
        if query:
               queryset_list = queryset_list.filter(
                   Q(work_name__company__company__icontains=query) |
                   Q(work_name__work_name__work_name__icontains=query)|
                   Q(work_result__icontains=query)
               ).distinct()
        elif self.request.GET.get('start_date') and self.request.GET.get('end_date') and self.request.GET.get('date'):
                if self.request.GET.get('date') =="업무마감일":
                    start_date1 = self.request.GET.get('start_date')
                    start_date = datetime.datetime.strptime(start_date1, '%Y-%m-%d')
                    end_date1 = self.request.GET.get('end_date')
                    end_date = datetime.datetime.strptime(end_date1, '%Y-%m-%d')
                    term = (start_date, end_date )
                    queryset_list = Result.objects.filter(work_date__range=term)
                elif self.request.GET.get('date') =="지원금 입금예정일":
                    start_date1 = self.request.GET.get('start_date')
                    start_date = datetime.datetime.strptime(start_date1, '%Y-%m-%d')
                    end_date1 = self.request.GET.get('end_date')
                    end_date = datetime.datetime.strptime(end_date1, '%Y-%m-%d')
                    term = (start_date, end_date + datetime.timedelta(days=1))
                    queryset_list = Result.objects.filter(amount_duedate__range=term)
                elif self.request.GET.get('date') =="지원금 입금일":
                    start_date1 = self.request.GET.get('start_date')
                    start_date = datetime.datetime.strptime(start_date1, '%Y-%m-%d')
                    end_date1 = self.request.GET.get('end_date')
                    end_date = datetime.datetime.strptime(end_date1, '%Y-%m-%d')
                    term = (start_date, end_date + datetime.timedelta(days=1))
                    queryset_list = Result.objects.filter(amount_date__range=term)

        else:
               queryset_list = queryset_list.all()
        return queryset_list



class Result_CreateView(LoginRequiredMixin,CreateView):
    model = Result
    form_class =ResultCreateForm
    template_name_suffix = '_create'

    def form_valid(self, form):
        form.instance.work_name = Working.objects.get(pk=self.kwargs.get('pk'))
        return super(Result_CreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('result_create', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['results'] = Working.objects.filter(pk=self.kwargs['pk'])
        context['resultslist'] = Result.objects.filter(work_name_id=self.kwargs['pk'])
        return context





class Result_UpdateView(LoginRequiredMixin, UpdateView):
    model = Result
    form_class = Result_UpaateForm
    template_name_suffix = '_update'


    def get_success_url(self, **kwargs):
        return reverse_lazy("result_create", args=(self.object.work_name_id,))


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['results'] = Working.objects.filter(pk=self.kwargs['pk'])
        context['resultslist'] = Result.objects.filter(pk=self.kwargs['pk'])
        return context




class Result_pay_listView(LoginRequiredMixin,ListView):
    model = Result
    fields = '__all__'
    paginate_by = 30
    ordering = ['created']

    def get_queryset(self, *args, **kwargs):

        queryset_list = Result.objects.select_related('work_name').filter(Q(work_result="입금완료"))
        query = self.request.GET.get("q")
        if query:
               queryset_list = queryset_list.filter(
                   Q(work_name__company__company__icontains=query) |
                   Q(work_name__work_name__work_name__icontains=query)|
                   Q(work_name__company__sales__name__icontains=query)
               ).distinct()
        elif self.request.GET.get('start_date') and self.request.GET.get('end_date') and self.request.GET.get('date'):
                if self.request.GET.get('date') =="지원금 입금":
                    start_date1 = self.request.GET.get('start_date')
                    start_date = datetime.datetime.strptime(start_date1, '%Y-%m-%d')
                    end_date1 = self.request.GET.get('end_date')
                    end_date = datetime.datetime.strptime(end_date1, '%Y-%m-%d')
                    term = (start_date, end_date )
                    queryset_list = Result.objects.filter(amount_date__range=term)
                elif self.request.GET.get('date') =="수수료 입금":
                    start_date1 = self.request.GET.get('start_date')
                    start_date = datetime.datetime.strptime(start_date1, '%Y-%m-%d')
                    end_date1 = self.request.GET.get('end_date')
                    end_date = datetime.datetime.strptime(end_date1, '%Y-%m-%d')
                    term = (start_date, end_date + datetime.timedelta(days=1))
                    queryset_list = Result.objects.filter(pay_date__range=term)
                elif self.request.GET.get('date') =="배당 지급":
                    start_date1 = self.request.GET.get('start_date')
                    start_date = datetime.datetime.strptime(start_date1, '%Y-%m-%d')
                    end_date1 = self.request.GET.get('end_date')
                    end_date = datetime.datetime.strptime(end_date1, '%Y-%m-%d')
                    term = (start_date, end_date + datetime.timedelta(days=1))
                    queryset_list = Result.objects.filter(fee_date__range=term)

        else:
               queryset_list = queryset_list.all()
        return queryset_list





class Result_pay_UpdateView(LoginRequiredMixin, UpdateView):
    model = Result
    form_class = Result_pay_UpaateForm
    template_name_suffix = '_update'


    def get_success_url(self, **kwargs):
        return reverse_lazy("result_pay_list")


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['resultslist'] = Result.objects.filter(pk=self.kwargs['pk'])
        return context


class Result_pay_dashboradlistView(LoginRequiredMixin,ListView):
    model = Result
    fields = '__all__'
    paginate_by = 30
    ordering = ['updated']



    def get_context_data(self, **kwargs):

        queryset_list = Result.objects.select_related('work_name').filter(Q(work_result="입금완료")).values('work_name__company__sales__name').order_by('work_name__company__sales__name').annotate(total_paycount=Count('pay'),total_pay=Sum('pay'), total_fee=Sum('fee'), total_feetax=Sum('fee_tax'))
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(work_name__company__sales__name__icontains=query)
            ).distinct()
        elif self.request.GET.get('start_date') and self.request.GET.get('end_date') and self.request.GET.get('date'):
            if self.request.GET.get('date') == "수수료입금":
                start_date1 = self.request.GET.get('start_date')
                start_date = datetime.datetime.strptime(start_date1, '%Y-%m-%d')
                end_date1 = self.request.GET.get('end_date')
                end_date = datetime.datetime.strptime(end_date1, '%Y-%m-%d')
                term = (start_date, end_date)
                queryset_list = Result.objects.filter(pay_date__range=term).values('work_name__company__sales__name').order_by('work_name__company__sales__name').annotate(total_paycount=Count('pay'),total_pay=Sum('pay'), total_fee=Sum('fee'), total_feetax=Sum('fee_tax'))
            elif self.request.GET.get('date') == "배당지급":
                start_date1 = self.request.GET.get('start_date')
                start_date = datetime.datetime.strptime(start_date1, '%Y-%m-%d')
                end_date1 = self.request.GET.get('end_date')
                end_date = datetime.datetime.strptime(end_date1, '%Y-%m-%d')
                term = (start_date, end_date + datetime.timedelta(days=1))
                queryset_list = Result.objects.filter(fee_date__range=term).values('work_name__company__sales__name').order_by('work_name__company__sales__name').annotate(total_paycount=Count('pay'),total_pay=Sum('pay'), total_fee=Sum('fee'), total_feetax=Sum('fee_tax'))

        else:
            queryset_list = queryset_list.all()

        context = {
            'queryset_list': queryset_list,
         }
        return context



class Result_nopay_listView(LoginRequiredMixin,ListView):
    model = Result
    fields = '__all__'
    paginate_by = 30
    ordering = ['created']

    def get_queryset(self, *args, **kwargs):

        queryset_list = Result.objects.select_related('work_name').filter(Q(work_result="입금완료")& Q(pay_date__isnull=True))
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(work_name__company__company__icontains=query) |
                Q(work_name__work_name__work_name__icontains=query) |
                Q(work_name__company__sales__name__icontains=query)
            ).distinct()
        elif self.request.GET.get('start_date') and self.request.GET.get('end_date') and self.request.GET.get('date'):
            if self.request.GET.get('date') == "지원금 입금":
                start_date1 = self.request.GET.get('start_date')
                start_date = datetime.datetime.strptime(start_date1, '%Y-%m-%d')
                end_date1 = self.request.GET.get('end_date')
                end_date = datetime.datetime.strptime(end_date1, '%Y-%m-%d')
                term = (start_date, end_date)
                queryset_list = Result.objects.filter(amount_date__range=term)
            elif self.request.GET.get('date') == "수수료 입금":
                start_date1 = self.request.GET.get('start_date')
                start_date = datetime.datetime.strptime(start_date1, '%Y-%m-%d')
                end_date1 = self.request.GET.get('end_date')
                end_date = datetime.datetime.strptime(end_date1, '%Y-%m-%d')
                term = (start_date, end_date + datetime.timedelta(days=1))
                queryset_list = Result.objects.filter(pay_date__range=term)
            elif self.request.GET.get('date') == "배당 지급":
                start_date1 = self.request.GET.get('start_date')
                start_date = datetime.datetime.strptime(start_date1, '%Y-%m-%d')
                end_date1 = self.request.GET.get('end_date')
                end_date = datetime.datetime.strptime(end_date1, '%Y-%m-%d')
                term = (start_date, end_date + datetime.timedelta(days=1))
                queryset_list = Result.objects.filter(fee_date__range=term)

        else:
            queryset_list = queryset_list.all()
        return queryset_list



class Dashborad_listView(LoginRequiredMixin,ListView):
    model = Result
    fields = '__all__'
    paginate_by = 30
    ordering = ['updated']




    def get_context_data(self, **kwargs):



        salesman = accounts_models.Sales.objects.all()
        customers = customers_models.Customer.objects.all()
        workings = Working.objects.filter(~Q(ing="계약완료")).all()
        working_result = Working.objects.filter(Q(ing="계약완료")).all()
        result_amount = Result.objects.filter(Q(work_result="입금완료") & Q(amount_date__isnull=False)).all()
        result_pay = Result.objects.filter(Q(work_result="입금완료") & Q(pay_date__isnull=False)).all()
        result_pay_no = Result.objects.filter(Q(work_result="입금완료") & Q(pay_date__isnull=True)).all()
        result_fee = Result.objects.filter(Q(work_result="입금완료")).all()


        if self.request.GET.get('start_date') and self.request.GET.get('end_date'):

            start_date1 = self.request.GET.get('start_date')
            start_date = datetime.datetime.strptime(start_date1, '%Y-%m-%d')
            end_date1 = self.request.GET.get('end_date')
            end_date = datetime.datetime.strptime(end_date1, '%Y-%m-%d')
            term = (start_date, end_date + datetime.timedelta(days=1))

            salesman =  accounts_models.Sales.objects.count()
            customers = customers_models.Customer.objects.count()
            workings = workings.filter(created__range=term).count()
            working_result = working_result.filter(updated__range=term).count()
            result_amount = result_amount.filter(amount_date__range=term).aggregate(total_amount=Sum('amount'))
            result_pay = result_pay.filter(pay_date__range=term).aggregate(total_pay=Sum('pay'))
            result_pay_no = result_pay_no.filter(pay_date__range=term).aggregate(total_pay=Sum('pay'))
            result_fee = result_fee.filter(fee_date__range=term).aggregate(total_pay=Sum('fee'))



        else:

            salesman = accounts_models.Sales.objects.count()
            customers = customers_models.Customer.objects.count()
            workings = Working.objects.filter(~Q(ing="계약완료")).count()
            working_result = Working.objects.filter(Q(ing="계약완료")).count()
            result_amount = Result.objects.filter(Q(work_result="입금완료") & Q(amount_date__isnull=False)).aggregate(total_amount=Sum('amount'))
            result_pay = Result.objects.filter(Q(work_result="입금완료") & Q(pay_date__isnull=False)).aggregate(total_pay=Sum('pay'))
            result_pay_no = Result.objects.filter(Q(work_result="입금완료") & Q(pay_date__isnull=True)).aggregate(total_pay=Sum('pay'))
            result_fee = Result.objects.filter(Q(work_result="입금완료")).aggregate(total_pay=Sum('fee'))

        context = {
                'salesman': salesman,
                'customers': customers,
                'workings': workings,
                'working_result': working_result,
                'result_amount': result_amount,
                'result_pay': result_pay,
                'result_pay_no': result_pay_no,
                'result_fee': result_fee,
                }
        context['salesman1'] = accounts_models.Sales.objects.all()
        return context



class Working_total_listView(LoginRequiredMixin,ListView):
    model = Working
    fields = '__all__'
    paginate_by = 30
    ordering = ['work_name']

    def get_queryset(self, *args, **kwargs):
        queryset_list = Working.objects.select_related('company').all()
        query = self.request.GET.get("q")
        if query:
               queryset_list = queryset_list.filter(
                   Q(company__company__icontains=query) |
                   Q(company__sales__name__icontains=query) |
                   Q(work_name__work_name__icontains=query) |
                   Q(ing__icontains=query)
               ).distinct()
        elif self.request.GET.get('start_date') and self.request.GET.get('end_date'):
                start_date1 = self.request.GET.get('start_date')
                start_date = datetime.datetime.strptime(start_date1, '%Y-%m-%d')
                end_date1 = self.request.GET.get('end_date')
                end_date = datetime.datetime.strptime(end_date1, '%Y-%m-%d')
                term = (start_date, end_date + datetime.timedelta(days=1))
                queryset_list = Working.objects.filter(created__range=term)
        else:
               queryset_list = queryset_list.all()
        return queryset_list



class Dashborad_amountlistView(LoginRequiredMixin,ListView):
    model = Result
    fields = '__all__'
    paginate_by = 30
    ordering = ['updated']

    def get_context_data(self, **kwargs):
        result_amount = Result.objects.filter(Q(work_result="입금완료")&Q(amount_date__isnull=False)).all()
        result_amount1 = Result.objects.filter(Q(work_result="입금완료") & Q(amount_date__isnull=True)).aggregate(total_amount1=Sum('amount'), total_amount_count1=Count('amount'))
        result_amount_work_name = Result.objects.filter(Q(work_result="입금완료")&Q(amount_date__isnull=False)).values('work_name__work_name').order_by('work_name__work_name').annotate(total_amount_count2=Count('amount'), total_amount2=Sum('amount'))
        result_amount_work_name1 = Result.objects.filter(Q(work_result="입금완료") & Q(amount_date__isnull=True)).values('work_name__work_name').order_by('work_name__work_name').annotate(total_amount_count2=Count('amount'),                                                                              total_amount2=Sum('amount'))
        result_amount_company = Result.objects.filter(Q(work_result="입금완료") & Q(amount_date__isnull=False)).values('work_name__company__company').order_by('work_name__company__company').annotate(total_amount_count3=Count('amount'), total_amount3=Sum('amount'))
        result_amount_company1 = Result.objects.filter(Q(work_result="입금완료") & Q(amount_date__isnull=True)).values('work_name__company__company').order_by('work_name__company__company').annotate(total_amount_count3=Count('amount'), total_amount3=Sum('amount'))

        if self.request.GET.get('start_date') and self.request.GET.get('end_date'):
            start_date1 = self.request.GET.get('start_date')
            start_date = datetime.datetime.strptime(start_date1, '%Y-%m-%d')
            end_date1 = self.request.GET.get('end_date')
            end_date = datetime.datetime.strptime(end_date1, '%Y-%m-%d')
            term = (start_date, end_date + datetime.timedelta(days=1))
            result_amount = result_amount.filter(amount_date__range=term).aggregate(total_amount=Sum('amount'), total_amount_count=Count('amount'))
            result_amount_work_name = result_amount_work_name.filter(amount_date__range=term).values('work_name__work_name').order_by('work_name__work_name').annotate(total_amount_count2=Count('amount'), total_amount2=Sum('amount'))
            result_amount_company = result_amount_company.filter(amount_date__range=term).values('work_name__company__company').order_by('work_name__company__company').annotate(total_amount_count3=Count('amount'), total_amount3=Sum('amount'))

        else:
            result_amount = Result.objects.filter(Q(work_result="입금완료") & Q(amount_date__isnull=False)).aggregate(total_amount=Sum('amount'), total_amount_count=Count('amount'))
            result_amount_work_name = Result.objects.filter(Q(work_result="입금완료") & Q(amount_date__isnull=False)).values('work_name__work_name').order_by('work_name__work_name').annotate(total_amount_count2=Count('amount'), total_amount2=Sum('amount'))
            result_amount_company = Result.objects.filter(Q(work_result="입금완료") & Q(amount_date__isnull=False)).values('work_name__company__company').order_by('work_name__company__company').annotate(total_amount_count3=Count('amount'), total_amount3=Sum('amount'))

        context = {

                'result_amount': result_amount,
                'result_amount1': result_amount1,
                'result_amount_work_name' : result_amount_work_name,
                'result_amount_work_name1' : result_amount_work_name1,
                'result_amount_company' : result_amount_company,
                'result_amount_company1': result_amount_company1,
                }

        return context

class Dashborad_paylistView(LoginRequiredMixin,ListView):
    model = Result
    fields = '__all__'
    paginate_by = 30
    ordering = ['updated']

    def get_context_data(self, **kwargs):
        result_pay = Result.objects.filter(Q(work_result="입금완료")&Q(pay_date__isnull=False)).all()
        result_pay1 = Result.objects.filter(Q(work_result="입금완료")&Q(pay_date__isnull=True)).aggregate(total_pay1=Sum('pay'), total_pay_count1=Count('pay'))
        result_pay_work_name = Result.objects.filter(Q(work_result="입금완료")&Q(pay_date__isnull=False)).values('work_name__work_name').order_by('work_name__work_name').annotate(total_pay_count2=Count('pay'), total_pay2=Sum('pay'))
        result_pay_work_name1 = Result.objects.filter(Q(work_result="입금완료") & Q(pay_date__isnull=True)).values('work_name__work_name').order_by('work_name__work_name').annotate(total_pay_count2=Count('pay'),total_pay2=Sum('pay'))
        result_pay_company = Result.objects.filter(Q(work_result="입금완료") & Q(pay_date__isnull=False)).values('work_name__company__company').order_by('work_name__company__company').annotate(total_pay_count3=Count('pay'), total_pay3=Sum('pay'))
        result_pay_company1 = Result.objects.filter(Q(work_result="입금완료") & Q(pay_date__isnull=True)).values('work_name__company__company').order_by('work_name__company__company').annotate(total_pay_count3=Count('pay'), total_pay3=Sum('pay'))

        if self.request.GET.get('start_date') and self.request.GET.get('end_date'):
            start_date1 = self.request.GET.get('start_date')
            start_date = datetime.datetime.strptime(start_date1, '%Y-%m-%d')
            end_date1 = self.request.GET.get('end_date')
            end_date = datetime.datetime.strptime(end_date1, '%Y-%m-%d')
            term = (start_date, end_date + datetime.timedelta(days=1))
            result_pay = result_pay.filter(pay_date__range=term).aggregate(total_amount=Sum('amount'))
            result_pay_work_name = result_pay_work_name.filter(pay_date__range=term).values('work_name__work_name').order_by('work_name__work_name').annotate(total_pay_count2=Count('pay'), total_pay2=Sum('pay'))
            result_pay_company = result_pay_company.filter(pay_date__range=term).values('work_name__company__company').order_by('work_name__company__company').annotate(total_pay_count2=Count('pay'), total_pay3=Sum('pay'))

        else:
            result_pay = Result.objects.filter(Q(work_result="입금완료") & Q(pay_date__isnull=False)).aggregate(total_pay=Sum('pay'), total_pay_count=Count('pay'))
            result_pay_work_name = Result.objects.filter(Q(work_result="입금완료") & Q(pay_date__isnull=False)).values('work_name__work_name').order_by('work_name__work_name').annotate(total_pay_count2=Count('pay'), total_pay2=Sum('pay'))
            result_pay_company = Result.objects.filter(Q(work_result="입금완료") & Q(pay_date__isnull=False)).values('work_name__company__company').order_by('work_name__company__company').annotate(total_pay_count3=Count('pay'), total_pay3=Sum('pay'))

        context = {

                'result_pay': result_pay,
                'result_pay1': result_pay1,
                'result_pay_work_name' : result_pay_work_name,
                'result_pay_work_name1': result_pay_work_name1,
                'result_pay_company' : result_pay_company,
                'result_pay_company1' : result_pay_company1,
                }

        return context



class Dashborad_feelistView(LoginRequiredMixin,ListView):
    model = Result
    fields = '__all__'
    paginate_by = 30
    ordering = ['updated']

    def get_context_data(self, **kwargs):
        now = datetime.date.today()
        nextmonth = now.month + 1
        result_fee = Result.objects.filter(Q(work_result="입금완료")&Q(fee_date__month__lte =now.month)).aggregate(total_fee=Sum('fee'), total_fee_count=Count('fee'))
        result_fee1 = Result.objects.filter(Q(work_result="입금완료")&Q(fee_date__month__gte=now.month)).aggregate(total_fee1=Sum('fee'), total_fee_count1=Count('fee'))
        result_fee2 = Result.objects.select_related('work_name').filter(Q(work_result="입금완료") & Q(fee_date__month=now.month)).values('work_name__company__sales__name').order_by('work_name__company__sales__name').annotate(total_fee_count2=Count('fee'), total_fee2=Sum('fee'), total_feetax2=Sum('fee_tax'))
        result_fee3 = Result.objects.select_related('work_name').filter(Q(work_result="입금완료") & Q(fee_date__month=nextmonth)).values('work_name__company__sales__name').order_by('work_name__company__sales__name').annotate(total_fee_count3=Count('fee'), total_fee3=Sum('fee'), total_feetax3=Sum('fee_tax'))


        if self.request.GET.get('start_date') and self.request.GET.get('end_date'):
            start_date1 = self.request.GET.get('start_date')
            start_date = datetime.datetime.strptime(start_date1, '%Y-%m-%d')
            end_date1 = self.request.GET.get('end_date')
            end_date = datetime.datetime.strptime(end_date1, '%Y-%m-%d')
            term = (start_date, end_date + datetime.timedelta(days=1))
            result_fee = result_fee.filter(fee_date__range=term).aggregate(total_fee=Sum('fee'), total_fee_count=Count('fee'))


        else:
            result_fee = Result.objects.filter(Q(work_result="입금완료") & Q(pay_date__isnull=False)).aggregate(total_pay=Sum('pay'), total_pay_count=Count('pay'))

        context = {
                'now': now,
                'nextmonth' : nextmonth,
                'result_fee': result_fee,
                'result_fee1': result_fee1,
                'result_fee2' : result_fee2,
                'result_fee3' : result_fee3,

                }

        return context




class Dashborad_sales_totallistView(LoginRequiredMixin,ListView):
    model = accounts_models.Sales
    fields = '__all__'
    paginate_by = 30


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_sales'] = accounts_models.Sales.objects.filter(pk=self.kwargs['pk'])
        context['total_customer_count'] = customers_models.Customer.objects.filter(sales__id=self.kwargs['pk']).aggregate(total_count=Count('company'))

        total = Result.objects.select_related('work_name').filter(work_name__company__sales__id=self.kwargs['pk'])
        context['total_result']  = total.filter(
            Q(work_result="입금완료")&Q(pay_date__isnull=False)).aggregate(total_amount_count=Count('amount'), total_amount=Sum('amount'),total_pay_count=Count('pay'), total_pay=Sum('pay'),total_fee_count=Count('fee'), total_fee=Sum('fee'),
                                                        total_feetax=Sum('fee_tax'))
        context['total_no_result'] = total.filter(Q(work_result="입금완료")&Q(pay_date__isnull=True)).aggregate(total_amount_count=Count('amount'), total_amount=Sum('amount'),
                                             total_pay_count=Count('pay'), total_pay=Sum('pay'),
                                             total_fee_count=Count('fee'), total_fee=Sum('fee'),
                                             total_feetax=Sum('fee_tax'))
        workings = Working.objects.select_related('work_name').filter(~Q(ing="계약완료"))
        working_result = Working.objects.select_related('work_name').filter(Q(ing="계약완료"))
        context['workings'] = workings.filter(company__sales__id=self.kwargs['pk']).aggregate(total_count=Count('work_name'))
        context['working_result'] = working_result.filter(company__sales__id=self.kwargs['pk']).aggregate(total_count=Count('work_name'))

        context['total_c'] = customers_models.Customer.objects.filter(sales__id=self.kwargs['pk'])
        context['total_w'] = workings.select_related('work_name').filter(company__sales__id=self.kwargs['pk'])
        context['total_rw'] = working_result.select_related('work_name').filter(company__sales__id=self.kwargs['pk'])
        context['total_r'] = Result.objects.select_related('work_name').filter(work_name__company__sales__id=self.kwargs['pk'])



        return context