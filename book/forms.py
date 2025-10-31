from django import forms
import re
from django.contrib.auth.models import User
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form__input', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form__input', "placeholder": "Password"}))

class RegisterForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form__input', "placeholder": "First Name"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form__input', "placeholder": "Last Name"}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form__input', "placeholder": "Username"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form__input', "placeholder": "Email"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form__input', "placeholder": "Password"}))
    reser_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form__input', "placeholder": "Reset password"}))

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if not username :
            raise forms.ValidationError("Username kiritilishi shart !")
        
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Bunday username mavjud !")
        

        return username
    

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if not email :
            raise forms.ValidationError("Email kiritilishi shart !")
        

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Bunday email mavjud !")
        
        return email
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if not first_name :
            raise forms.ValidationError("First name kiritilish shart !")
        
        if len(first_name) < 3:
            raise forms.ValidationError("First name 3 ta harfdan kam bo'lmashlgi kerak !")
        
        if not re.match(r'^[A-Za-zА-Яа-яЁёІіЇїĞğÜüŞşÖöÇçƏə\s-]+$', first_name):
            raise forms.ValidationError("First name faqat harflardan iborat bo'lishi kerak !")
        
        return first_name
    
    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')

        if not last_name :
            raise forms.ValidationError("Last name kiritilish shart !")
        
        if len(last_name) < 3:
            raise forms.ValidationError("Last name 3 ta harfdan kam bo'lmashlgi kerak !")
        
        if not re.match(r'^[A-Za-zА-Яа-яЁёІіЇїĞğÜüŞşÖöÇçƏə\s-]+$', last_name):
            raise forms.ValidationError("Last name faqat harflardan iborat bo'lishi kerak !")
        
        return last_name
    
    def clean_reset_password(self):
        password = self.cleaned_data.get('password')
        reset_password = self.cleaned_data.get('reser_password')
        pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

        if  not reset_password :
            raise forms.ValidationError("Reset password kiritilishi shart!")
        
        if password != reset_password:
            raise forms.ValidationError("Parollar mos emas !")
        
        if not password :
            raise forms.ValidationError("Parol kiritilishi shar !")
        
        if re.match(pattern, password) is None:
            raise forms.ValidationError("Parol kamida 8 ta belgidan iborat bo'lishi kerak, kamida bitta katta harf, bitta kichik harf, bitta raqam va bitta maxsus belgi bo'lishi kerak !")
        return reset_password