from django.db import models
from django.contrib.auth.models import AbstractUser
from .models import *
import datetime



class Account(AbstractUser):

    user_name = models.CharField('이름', max_length=50)
    team = models.CharField('소속', max_length=50, null=True, blank=True,)
    phone = models.CharField('연락처', max_length=50, null=True, blank=True,)
    time_stamp = models.DateTimeField('등록일', default=datetime.datetime.now(), editable=False)



class Sales(models.Model):

    name = models.CharField('이름', max_length=50)
    team = models.CharField('소속', max_length=50, null=True, blank=True,)
    phone = models.CharField('연락처', max_length=50, null=True, blank=True,)
    time_stamp = models.DateTimeField('등록일', default=datetime.datetime.now(), editable=False)
    referrer_name = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True, related_name='sales')
    memo = models.TextField('메모', blank=True)

    class Meta:
        ordering = ['time_stamp']

    def __str__(self):
        return self.name
