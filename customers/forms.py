from django import forms
from .models import *



class CustomerCreateForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields =  ['category','company','name','phone','location','address','memo','sub_company','sales']
    def __init__(self, *args, **kwargs):
        super(CustomerCreateForm, self).__init__(*args, **kwargs)
    # 각 input 태그의 help_text, label을 제거함.
        for field in self.fields:
            self.fields[field].help_text = None
            self.fields[field].label = ''
            # 각 input 태그에 placeholder를 추가함.
            self.fields['company'].widget.attrs = {'placeholder': '회사상호를 적어주세요', 'autocomplete': 'off'}
            self.fields['name'].widget.attrs = {'placeholder': '대표자명을 적어주세요', 'autocomplete': 'off'}
            self.fields['phone'].widget.attrs = {'placeholder': '010-0000-0000 형식으로', 'autocomplete': 'off'}
            self.fields['address'].widget.attrs = {'placeholder': '전체 주소(상세)를 적어주세요', 'autocomplete': 'off'}
            self.fields['memo'].widget.attrs = {'placeholder': '업체메모', 'autocomplete': 'off'}



class Customer_UpaateForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields =  ['category','company','name','phone','location','address','memo','sub_company','sales']
    def __init__(self, *args, **kwargs):
        super(Customer_UpaateForm, self).__init__(*args, **kwargs)
    # 각 input 태그의 help_text, label을 제거함.
        for field in self.fields:
            self.fields[field].help_text = None
            self.fields[field].label = ''
            # 각 input 태그에 placeholder를 추가함.
            self.fields['company'].widget.attrs = {'placeholder': '회사상호를 적어주세요', 'autocomplete': 'off'}
            self.fields['name'].widget.attrs = {'placeholder': '대표자명을 적어주세요', 'autocomplete': 'off'}
            self.fields['phone'].widget.attrs = {'placeholder': '010-0000-0000 형식으로', 'autocomplete': 'off'}
            self.fields['address'].widget.attrs = {'placeholder': '전체 주소(상세)를 적어주세요', 'autocomplete': 'off'}
            self.fields['memo'].widget.attrs = {'placeholder': '업체메모', 'autocomplete': 'off'}