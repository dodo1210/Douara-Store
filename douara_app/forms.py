# -*- coding: utf 8 -*-
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class RegisterForm(UserCreationForm):
	email = forms.EmailField(label = 'E-mail',widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Email'}))
	username = forms.CharField(label = 'Usuário',widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Nome completo'}))
	password1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','type': 'password','placeholder':'Senha'}))
	password2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','type': 'password', 'placeholder':'Confirmar senha'}))

	def save(self,  commit = True):
		user = super(RegisterForm, self).save(commit = False)
		user.email = self.cleaned_data['email']
		user.first_name = self.cleaned_data['username']
		if commit:
			user.save()
		return user

class UserProfile(forms.ModelForm):
	CPF_CNPJ = forms.CharField(label = 'CPF/CNPJ',widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'CNPJ/CPF'}))
	rua = forms.CharField(label = 'RUA',widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'RUA'}))
	numero = forms.CharField(label = 'NÚMERO',widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Número'}))
	CEP = forms.CharField(label = 'CEP',widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'CEP'}))
	fone = forms.CharField(label = 'Telefone',widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Telefone'}))
	complemento = forms.CharField(label = 'Complemento',widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Complemento'}))
	
	class Meta:
		model = UserProfile
		fields = ['CPF_CNPJ','rua','numero','CEP','fone','complemento']
		widgets = {'class': 'form-control'}
		

