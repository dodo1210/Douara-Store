from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User, AbstractUser
from .models import UserProfile as UserProfiles
from django.contrib import admin
from .forms import *
from django.template import RequestContext
from rest_framework.authtoken.models import Token
from django.contrib import auth
from django.template.context_processors import csrf

	
class Home(TemplateView):
    template_name = "home.html"

class Categoria(TemplateView):
    template_name = "shop.html"

class Produto(TemplateView):
    template_name = "product-details.html"

class Finalizar(TemplateView):
	template_name = 'checkout.html'
	model = UserProfiles
	initial = {'form': UserProfile}
	fields = ['CPF_CNPJ','rua','numero','CEP','fone','complemento']
	
	def get(self, request,pk):
		return render(request, self.template_name, {'form': UserProfile, 'user':User.objects.filter(id=pk)[0]})
	
	def post(self, request,pk):
		form = UserProfile(request.POST or None)
		print(form)
		print(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
		else:
			print("oh")
			return HttpResponseRedirect('/')
		return HttpResponseRedirect('/')


class Carrinho(TemplateView):
    template_name = "cart.html"

def register(request):
  if request.method == "POST":
    form = RegisterForm(request.POST)
    if form.is_valid():
      form.save()
      user = User.objects.all().last()
      return HttpResponseRedirect('')
  else:
    form = RegisterForm()
  context = {
    'form' : form
  }
  return render(request,'cadastrar.html',context)

def login_compra(request):
  print(request.POST.get('username',''))
  print(request.POST.get('password',''))
  user  = auth.authenticate(username=request.POST.get('username',''), password=request.POST.get('password',''))
  print(user)
  if user is not None:
    auth.login(request, user)
    print("oi")
    return HttpResponseRedirect('/finalizar/'+str(user.id))
  else:
    c = {}
    c.update(csrf(request))
    c.update({'error_message': 'Senha ou Usuario Incorretos'})
    return render(request, 'login.html', c)

def logout(request):
  c = {}
  c.update(csrf(request))
  auth.logout(request)
  return HttpResponseRedirect('/')

def auth_view(request):
  print(request.POST.get('username',''))
  print(request.POST.get('password',''))
  user  = auth.authenticate(username=request.POST.get('username',''), password=request.POST.get('password',''))
  print(user)
  if user is not None:
    auth.login(request, user)
    print("oi")
    return HttpResponseRedirect('/finalizar')
  else:
    c = {}
    c.update(csrf(request))
    c.update({'error_message': 'Senha ou Usuario Incorretos'})
    return render(request, 'login_para_comprar.html', c)

def logout(request):
  c = {}
  c.update(csrf(request))
  auth.logout(request)
  return HttpResponseRedirect('/')