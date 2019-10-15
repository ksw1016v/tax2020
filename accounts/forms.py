from django import forms
from .models import *


# 회원가입 폼
class RegisterForm(forms.ModelForm):
    password = forms.CharField(label="PASSWORD", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat PASSWORD", widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ['username', 'user_name', 'team','phone','email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('PASSWORD NOT MATCHED!!!!!')
        return cd['password2']

    def __init__(self, *args, **kwargs):
         super(RegisterForm, self).__init__(*args, **kwargs)
    # 각 input 태그의 help_text, label을 제거함.
         for field in self.fields:
                self.fields[field].help_text = None
                self.fields[field].label = ''
    # 각 input 태그에 placeholder를 추가함.
                self.fields['username'].widget.attrs={ 'placeholder': 'ID는 영어와 숫자' , 'autocomplete':'off'}
                self.fields['user_name'].widget.attrs={ 'placeholder': '이름은 한글로 적어주세요' , 'autocomplete':'off'}
                self.fields['team'].widget.attrs={'placeholder': '팀' , 'autocomplete':'off'}
                self.fields['phone'].widget.attrs={'placeholder': '휴대폰번호는 010-0000-0000 형식' , 'autocomplete':'off'}
                self.fields['email'].widget.attrs={'placeholder': 'Email Address' , 'autocomplete':'off'}


class Sales_CreateForm(forms.ModelForm):
    class Meta:
        model = Sales
        fields = ['name', 'team', 'phone', 'memo','referrer_name']

    def __init__(self, *args, **kwargs):
        super(Sales_CreateForm, self).__init__(*args, **kwargs)
        # 각 input 태그의 help_text, label을 제거함.
        for field in self.fields:
            self.fields[field].help_text = None
            self.fields[field].label = ''
            # 각 input 태그에 placeholder를 추가함.
            self.fields['name'].widget.attrs = {'placeholder': '이름을 적어주세요', 'autocomplete': 'off'}
            self.fields['team'].widget.attrs = {'placeholder': '소속을 적어주세요', 'autocomplete': 'off'}
            self.fields['phone'].widget.attrs = {'placeholder': '010-0000-0000 형식으로', 'autocomplete': 'off'}
            self.fields['memo'].widget.attrs = {'placeholder': '메모', 'autocomplete': 'off'}


class Sales_UpaateForm(forms.ModelForm):
    class Meta:
        model = Sales
        fields = ['name', 'team', 'phone', 'memo','referrer_name']

    def __init__(self, *args, **kwargs):
        super(Sales_UpaateForm, self).__init__(*args, **kwargs)
        # 각 input 태그의 help_text, label을 제거함.
        for field in self.fields:
            self.fields[field].help_text = None
            self.fields[field].label = ''
            # 각 input 태그에 placeholder를 추가함.
            self.fields['name'].widget.attrs = {'placeholder': '이름을 적어주세요', 'autocomplete': 'off'}
            self.fields['team'].widget.attrs = {'placeholder': '소속을 적어주세요', 'autocomplete': 'off'}
            self.fields['phone'].widget.attrs = {'placeholder': '010-0000-0000 형식으로', 'autocomplete': 'off'}
            self.fields['memo'].widget.attrs = {'placeholder': '메모', 'autocomplete': 'off'}













