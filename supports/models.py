from django.db import models
import datetime
from accounts import models as accounts_models
from customers import models as customers_models
from decimal import Decimal

# Create your models here.


class Work(models.Model):
    work_name = models.CharField('사업명',max_length=50, unique=True)
    Requirements1= models.CharField('요구사항1',max_length=50,null=True, blank=True)
    Requirements2 = models.CharField('요구사항2',max_length=50,null=True, blank=True)
    Requirements3 = models.CharField('요구사항3', max_length=50, null=True, blank=True)
    support_period = models.FloatField('사업기간',null=True, blank=True)
    support_amount = models.FloatField('지원금액/월', null=True, blank=True)
    memo = models.TextField('참고사항',null=True, blank=True)

    class Meta:
        ordering = ['work_name']


    def __str__(self):
        return self.work_name







class Working(models.Model):
    A1 = '상담대기'
    A2 = '방문약속'
    A3 = '해당안됨'
    A4 = '고민후연락'
    A5 = '재방문요청'
    A6 = '계약완료'
    A7 = '거절'
    A8 = '삭제요청'
    ing_choices = (
        (A1, '상담대기'),
        (A2, '방문약속'),
        (A3, '해당안됨'),
        (A4, '고민후연락'),
        (A5, '재방문요청'),
        (A6, '계약완료'),
        (A7, '거절'),
        (A8, '삭제요청'),
    )

    company = models.ForeignKey(customers_models.Customer, on_delete=models.CASCADE, related_name="workings")
    work_name= models.ForeignKey(Work, on_delete=models.CASCADE,related_name="workings", to_field='work_name',verbose_name='사업명')
    ing = models.CharField('진행',max_length=6, choices=ing_choices, default=A1)
    support_amount = models.DecimalField('지원금', blank=True, null=True, max_digits=12, decimal_places=0)
    created = models.DateTimeField('등록일', default=datetime.datetime.now(), editable=False)
    updated = models.DateTimeField('수정일',auto_now=True)
    pay_per = models.DecimalField('수수료율', blank=True, max_digits=12, decimal_places=2, default=Decimal('0'))
    fee_per = models.DecimalField('배당률', blank=True, max_digits=12, decimal_places=2, default=Decimal('0'))
    memo = models.TextField('진행사항', null=True, blank=True)

    class Meta:
        ordering = ['-created']


    def __str__(self):
        return self.ing






class Result(models.Model):
    C1 = '신청서'
    C2 = '서류심사'
    C3 = '승인실사'
    C4 = '4대보험취득'
    C5 = '지원금신청'
    C6 = '기타'
    work_choices = (
        (C1, '신청서'),
        (C2, '서류심사'),
        (C3, '승인실사'),
        (C4, '4대보험취득'),
        (C5, '지원금신청'),
        (C6, '기타'),
    )
    A1 = '진행'
    A2 = '보류'
    A3 = '승인'
    A4 = '불승인'
    A5 = '완료'
    A6 = '입금완료'
    A7 = '취소'
    ing_choices = (
        (A1, '진행'),
        (A2, '보류'),
        (A3, '승인'),
        (A4, '불승인'),
        (A5, '완료'),
        (A6, '입금완료'),
        (A7, '취소'),
    )

    work_name = models.ForeignKey(Working, on_delete=models.CASCADE, related_name="results")
    work_date = models.DateField('업무마감일', null=True, blank=True)
    work_category = models.CharField('업무내용', max_length=50,  choices=work_choices, default=C1)
    work_result = models.CharField('업무결과', max_length=50, choices=ing_choices, default=A1)
    amount = models.DecimalField('신청지원금', blank=True,  max_digits=12, decimal_places=0, default=Decimal('0'))
    amount_duedate = models.DateField('지원금입금예정', null=True, blank=True)
    amount_date = models.DateField('지원금입금일', null=True, blank=True)
    amount_memo = models.TextField('지원금메모', null=True, blank=True)
    created = models.DateTimeField('등록일', default=datetime.datetime.now(), editable=False)
    updated = models.DateTimeField('수정일시', auto_now=True)
    pay = models.DecimalField('수수료', blank=True, max_digits=12, decimal_places=0)
    pay_date = models.DateField('수수료입금일', null=True, blank=True)
    pay_memo = models.TextField('수수료메모', null=True, blank=True)
    fee = models.DecimalField('배당', blank=True,  max_digits=12, decimal_places=0)
    fee_tax = models.DecimalField('지급액', blank=True,  max_digits=12, decimal_places=0)
    fee_date = models.DateField('배당지급일', null=True, blank=True)
    fee_memo = models.TextField('배당메모', null=True, blank=True)


    class Meta:
        ordering = ['work_name', 'work_date']

    @property
    def get_pay(self):
        pay_per = self.work_name.pay_per
        pay = (pay_per) * (self.amount) / 100
        return pay

    @property
    def get_fee(self):
        pay = self.pay
        fee_per = self.work_name.fee_per
        fee = (fee_per) * (pay) / 100
        return fee

    @property
    def get_fee_tax(self):
        fee = self.fee
        fee_tax = (fee)- (fee) * 33 / 10000
        return fee_tax


    def save(self, *args, **kwargs):
        self.pay = self.get_pay
        self.fee = self.get_fee
        self.fee_tax = self.get_fee_tax
        super(Result, self).save(*args, **kwargs)

