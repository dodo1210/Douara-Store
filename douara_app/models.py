from django.db import models
from django.utils import timezone
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import Permission, User
from datetime import datetime
from PIL import Image
from django.db.models.signals import post_save

class UserProfile(models.Model):  
    CEP = models.CharField(max_length=8, blank=True)
    rua =  models.CharField(max_length=60, blank=True)
    numero = models.CharField(max_length=10, blank=True)
    complemento = models.CharField(max_length=60, blank=True)
    fone = models.CharField(max_length=12, blank=True)
    CPF_CNPJ = models.CharField(max_length=18, blank=True, primary_key = True) 

class Produto(models.Model):
	def user_directory_path(instance, filename): 
  		return 'douara_app/static/img/Produto/{0}'.format(filename)

	nome = models.CharField(max_length=60, blank=True, primary_key = True, default=True)
	tamanho = models.CharField(max_length=3, blank=True)
	cor = models.CharField(max_length=20, blank=True)
	categoria = models.CharField(max_length=20, blank=True)
	lançamento = models.BooleanField(default=False)
	tamanho = models.CharField(max_length=5, blank=True)
	quantidade = models.IntegerField(null=True,blank=True)
	preço = models.FloatField(null=True,blank=True)
	promoção = models.FloatField(null=True,blank=True)
	data_lançamento = models.DateTimeField(verbose_name='Data de Lançamento',default=timezone.now,blank=True)
	imagem = models.ImageField(upload_to = user_directory_path, height_field=None, width_field=None, max_length=100)
	imagem_hover = models.ImageField(upload_to = user_directory_path, height_field=None, width_field=None, max_length=100, default=True)

class Carrinho(models.Model):
	user = models.OneToOneField(User,on_delete = models.CASCADE, primary_key = True)
	produto =  models.ManyToManyField(Produto)
	frete = models.FloatField(null=True,blank=True)
	quantidade = models.CharField(max_length=100, blank=True)
   
