from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class ContactForm(forms.Form):
    name = forms.CharField(
        label='Ваше имя',
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'my-input',
                'placeholder': 'Ваше имя',
                'required': True
            }))
    phone = forms.CharField(
        label='Ваш номер телефона',
        max_length=20,
        widget=forms.TextInput(
            attrs={
                'class': 'my-input',
                'id': 'phone',
                'name': 'phone',
                'placeholder': 'Ваш номер телефона',
                'required': True}))


class OrderForm(forms.Form):
    name = forms.CharField(
        label='Ваше имя',
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'my-input',
                'placeholder': 'Ваше имя',
                'required': True
            }))
    phone = forms.CharField(
        label='Ваш номер телефона',
        max_length=20,
        widget=forms.TextInput(
            attrs={
                'class': 'my-input',
                'id': 'phone',
                'name': 'phone',
                'placeholder': 'Ваш номер телефона',
                'required': True
            }))
    email = forms.CharField(
        label='Как вас зовут?',
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'my-input',
                'name': 'email',
                'placeholder': 'Email',
                'required': False,
            }
        ))
    budget = forms.CharField(
        label='Ваш ориентировочный бюджет',
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'my-input',
                'name': 'budget',
                'id': 'budget',
                'placeholder': 'Ваш ориентировочный бюджет',
                'required': True,
            }
        ))

    task = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'my-textarea',
                'name': 'task',
                'id': 'task',
                'placeholder': 'Опишите задачу',
                'required': True,
            }
        ))
