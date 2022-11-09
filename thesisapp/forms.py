from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForms(UserCreationForm):
    class Meta:
        model = User
        fields=[]
        widgets = {
            'pid': forms.TextInput(attrs={'class': 'form-control', 'size': 15, 'maxlength': 13}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'size': 55, 'maxlength': 50}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'Min': 1}),
            'net': forms.NumberInput(attrs={'class': 'form-control', 'Min': 0}),
            'picture': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
        }
        labels = {
            'pid': 'รหัสสินค้า',
            'name': 'ชื่อสินค้า',
            'category': 'ประเภทสินค้า',
            'price': 'ราคาต่อหน่วย',
            'net': 'คงเหลือ',
            'picture': 'ภาพสินค้า',
        }

class RegisterForms(forms.ModelForm):
    class Meta:
        model = au
        fields = ('pid', 'name', 'category', 'price', 'net', 'picture', )
        widgets = {
            'pid': forms.TextInput(attrs={'class': 'form-control',  'size':15, 'maxlength':13}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'size':55, 'maxlength':50}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'Min': 1}),
            'net': forms.NumberInput(attrs={'class': 'form-control', 'Min': 0}),
            'picture':forms.FileInput(attrs={'class': 'form-control', 'accept':'image/*'}),
        }
        labels = {
            'pid': 'รหัสสินค้า',
            'name': 'ชื่อสินค้า',
            'category': 'ประเภทสินค้า',
            'price': 'ราคาต่อหน่วย',
            'net': 'คงเหลือ',
            'picture': 'ภาพสินค้า',
        }

    def updateForm(self):
        self.fields['pid'].widget.attrs['readonly'] = True
        self.fields['pid'].label = 'รหัสสินค้า [ไม่อนุญาตให้แก้ไขได้]'

    def deleteForm(self):
        self.fields['pid'].widget.attrs['readonly'] = True
        self.fields['name'].widget.attrs['readonly'] = True
        self.fields['category'].widget.attrs['readonly'] = True
        self.fields['price'].widget.attrs['readonly'] = True
        self.fields['net'].widget.attrs['readonly'] = True
        self.fields['picture'].widget.attrs['readonly'] = True
