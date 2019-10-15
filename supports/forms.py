from django import forms
from .models import *



class WorkCreateForm(forms.ModelForm):
    class Meta:
        model = Work
        fields =  ['work_name','Requirements1','Requirements2','Requirements3','support_period','support_amount','memo']
    def __init__(self, *args, **kwargs):
        super(WorkCreateForm, self).__init__(*args, **kwargs)
    # 각 input 태그의 help_text, label을 제거함.
        for field in self.fields:
            self.fields[field].help_text = None
            self.fields[field].label = ''
            # 각 input 태그에 placeholder를 추가함.
            self.fields['work_name'].widget.attrs = {'placeholder': '지원사업명을 적어주세요', 'autocomplete': 'off'}
            self.fields['Requirements1'].widget.attrs = {'placeholder': '요구사항1', 'autocomplete': 'off'}
            self.fields['Requirements2'].widget.attrs = {'placeholder': '요구사항2', 'autocomplete': 'off'}
            self.fields['Requirements3'].widget.attrs = {'placeholder': '요구사항3', 'autocomplete': 'off'}
            self.fields['support_period'].widget.attrs = {'placeholder': '사업기간', 'autocomplete': 'off'}
            self.fields['support_amount'].widget.attrs = {'placeholder': '지원금액/월', 'autocomplete': 'off'}
            self.fields['memo'].widget.attrs = {'placeholder': '참고사항', 'autocomplete': 'off'}


class WorkUpdateForm(forms.ModelForm):
    class Meta:
        model = Work
        fields =  ['work_name','Requirements1','Requirements2','Requirements3','support_period','support_amount','memo']
    def __init__(self, *args, **kwargs):
        super(WorkUpdateForm, self).__init__(*args, **kwargs)
    # 각 input 태그의 help_text, label을 제거함.
        for field in self.fields:
            self.fields[field].help_text = None
            self.fields[field].label = ''
            # 각 input 태그에 placeholder를 추가함.
            self.fields['work_name'].widget.attrs = {'placeholder': '지원사업명을 적어주세요', 'autocomplete': 'off'}
            self.fields['Requirements1'].widget.attrs = {'placeholder': '요구사항1', 'autocomplete': 'off'}
            self.fields['Requirements2'].widget.attrs = {'placeholder': '요구사항2', 'autocomplete': 'off'}
            self.fields['Requirements3'].widget.attrs = {'placeholder': '요구사항3', 'autocomplete': 'off'}
            self.fields['support_period'].widget.attrs = {'placeholder': '사업기간', 'autocomplete': 'off'}
            self.fields['support_amount'].widget.attrs = {'placeholder': '지원금액/월', 'autocomplete': 'off'}
            self.fields['memo'].widget.attrs = {'placeholder': '참고사항', 'autocomplete': 'off'}





class Work_add_CreateForm(forms.ModelForm):

    class Meta:
        model = Working
        fields = [ 'work_name','ing','support_amount','pay_per','fee_per','memo']




class Working_upaate_CreateForm(forms.ModelForm):

    class Meta:
        model = Working
        fields = [ 'work_name','ing','support_amount','pay_per','fee_per','memo']



class ResultCreateForm(forms.ModelForm):

    class Meta:
        model = Result
        fields =  ['work_date','work_category','work_result','amount','amount_duedate','amount_date','amount_memo']
        widgets = {
            'work_date': forms.DateInput(attrs={'type': 'date'}),
            'amount_duedate': forms.DateInput(attrs={'type': 'date'}),
            'amount_date': forms.DateInput(attrs={'type': 'date'})
        }
    def __init__(self, *args, **kwargs):
        super(ResultCreateForm, self).__init__(*args, **kwargs)
    # 각 input 태그의 help_text, label을 제거함.
        for field in self.fields:
            self.fields[field].help_text = None
            self.fields[field].label = ''
            # 각 input 태그에 placeholder를 추가함.

            self.fields['work_date'].widget.attrs = {'placeholder': '업무마감일', 'autocomplete': 'off'}
            self.fields['work_category'].widget.attrs = {'placeholder': '업무내용', 'autocomplete': 'off'}
            self.fields['work_result'].widget.attrs = {'placeholder': '업무결과', 'autocomplete': 'off'}
            self.fields['amount'].widget.attrs = {'placeholder': '신청지원금', 'autocomplete': 'off'}
            self.fields['amount_duedate'].widget.attrs = {'placeholder': '지원금입금예정일', 'autocomplete': 'off'}
            self.fields['amount_date'].widget.attrs = {'placeholder': '지원금입금일', 'autocomplete': 'off'}
            self.fields['amount_memo'].widget.attrs = {'placeholder': '지원금메모', 'autocomplete': 'off'}




class Result_UpaateForm(forms.ModelForm):

    class Meta:
        model = Result
        fields = ['work_date', 'work_category', 'work_result', 'amount', 'amount_duedate', 'amount_date', 'amount_memo']
        widgets = {
            'work_date': forms.DateInput(attrs={'type': 'date'}),
            'amount_duedate': forms.DateInput(attrs={'type': 'date'}),
            'amount_date': forms.DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super(Result_UpaateForm, self).__init__(*args, **kwargs)
        # 각 input 태그의 help_text, label을 제거함.
        for field in self.fields:
            self.fields[field].help_text = None
            self.fields[field].label = ''
            # 각 input 태그에 placeholder를 추가함.

            self.fields['work_date'].widget.attrs = {'placeholder': '업무마감일', 'autocomplete': 'off'}
            self.fields['work_category'].widget.attrs = {'placeholder': '업무내용', 'autocomplete': 'off'}
            self.fields['work_result'].widget.attrs = {'placeholder': '업무결과', 'autocomplete': 'off'}
            self.fields['amount'].widget.attrs = {'placeholder': '신청지원금', 'autocomplete': 'off'}
            self.fields['amount_duedate'].widget.attrs = {'placeholder': '지원금입금예정일', 'autocomplete': 'off'}
            self.fields['amount_date'].widget.attrs = {'placeholder': '지원금입금일', 'autocomplete': 'off'}
            self.fields['amount_memo'].widget.attrs = {'placeholder': '지원금메모', 'autocomplete': 'off'}





class Result_pay_UpaateForm(forms.ModelForm):

    class Meta:
        model = Result
        fields = ['pay', 'pay_date', 'pay_memo', 'fee', 'fee_date', 'fee_memo']
        widgets = {
            'pay_date': forms.DateInput(attrs={'type': 'date'}),
            'fee_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(Result_pay_UpaateForm, self).__init__(*args, **kwargs)
        # 각 input 태그의 help_text, label을 제거함.
        for field in self.fields:
            self.fields[field].help_text = None
            self.fields[field].label = ''
            # 각 input 태그에 placeholder를 추가함.

            self.fields['pay'].widget.attrs = {'placeholder': '수수료', 'autocomplete': 'off'}
            self.fields['pay_date'].widget.attrs = {'placeholder': '수수료입금일', 'autocomplete': 'off'}
            self.fields['pay_memo'].widget.attrs = {'placeholder': '수수료 메모', 'autocomplete': 'off'}
            self.fields['fee'].widget.attrs = {'placeholder': '배당금', 'autocomplete': 'off'}
            self.fields['fee_date'].widget.attrs = {'placeholder': '배당지급일', 'autocomplete': 'off'}
            self.fields['fee_memo'].widget.attrs = {'placeholder': '배당 메모', 'autocomplete': 'off'}
