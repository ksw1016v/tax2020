from django.db import models
import datetime
from accounts import models as accounts_models


class Customer(models.Model):
    C1 = '내부'
    C2 = '외부'

    category_choices = (
        (C1, '내부'),
        (C2, '외부'),
    )
    L1 = '부산'
    L2 = '김해'
    L3 = '양산'
    L4 = '창원'
    L5 = '울산'
    L6 = '거제/통영'
    L7 = '기타'

    location_choices = (
        (L1, '부산'),
        (L2, '김해'),
        (L3, '양산'),
        (L4, '창원'),
        (L5, '울산'),
        (L6, '거제/통영'),
        (L7, '기타'),
    )
    B0 = "비사업자"
    B1 = '제조'
    B2 = '건설'
    B3 = '도소매'
    B4 = '음식/숙박'
    B5 = '부동산'
    B6 = '교육'
    B7 = '운수'
    B8 = '기타'

    bizsub_choices = (
        (B0, '비사업자'),
        (B1, '제조'),
        (B2, '건설'),
        (B3, '도소매'),
        (B4, '음식/숙박'),
        (B5, '부동산'),
        (B6, '교육'),
        (B7, '운수'),
        (B8, '기타'),
    )
    time_stamp = models.DateTimeField('등록일', default=datetime.datetime.now(), editable=False)
    company = models.CharField('회사명', max_length=50)
    category = models.CharField('구분',max_length=6, choices=category_choices, default=C2)
    sales = models.ForeignKey(accounts_models.Sales, on_delete=models.SET_NULL, null=True,blank=True, related_name="customers")
    name = models.CharField('이름', max_length=50)
    phone = models.CharField('연락처',max_length=50)
    location = models.CharField('지역',max_length=100,choices=location_choices, default=L1)
    address = models.CharField('주소',max_length=100)
    bizsub = models.CharField('업종',max_length=6, choices=bizsub_choices, default=B0)
    memo = models.TextField('메모',blank=True)
    sub_company = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True, related_name='sub')


    class Meta:
        ordering = ['time_stamp']

    def __str__(self):
        return self.company