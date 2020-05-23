from django import forms
from .models import Info
from utils.forms import FormMixin


class InfoCreateForm(forms.ModelForm, FormMixin):
    class Meta:
        model = Info
        exclude = ['is_delete']
        widgets = {
            'xh': forms.TextInput(attrs={'class': 'form-control'}),
            'pwd': forms.TextInput(attrs={'class': 'form-control'}),
            'sfhx': forms.Select(attrs={'class': 'form-control'}),
            'dqszdsm': forms.TextInput(attrs={'class': 'form-control'}),
            'dqszddjsm':forms.TextInput(attrs={'class': 'form-control'}),
            'dqszdxjsm':forms.TextInput(attrs={'class': 'form-control'}),
            'dqszdxxdz': forms.TextInput(attrs={'class': 'form-control'}),
            'sfqwhb14': forms.Select(attrs={'class': 'form-control'}),
            'sfjchb14': forms.Select(attrs={'class': 'form-control'}),
            'sfqwjw14': forms.Select(attrs={'class': 'form-control'}),
            'sfjcjw14': forms.Select(attrs={'class': 'form-control'}),
             'jrtw': forms.TextInput(attrs={'class': 'form-control'}),
              'sfczzz':       forms.Select(attrs={'class': 'form-control'}),
            'dwdzxx': forms.TextInput(attrs={'class': 'form-control'}),
            'dwjd': forms.TextInput(attrs={'class': 'form-control'}),
            'dwwd': forms.TextInput(attrs={'class': 'form-control'}),
             'yqzd':    forms.Select(attrs={'class': 'form-control'}),
            'jkm': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'})
        }