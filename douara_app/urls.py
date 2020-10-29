from django.conf.urls import url
from . import views

app_name = 'douara_app'

urlpatterns = [
	url(r'^categoria$', views.Categoria.as_view()),
	url(r'^finalizar/(?P<pk>[-\w]+)$', views.Finalizar.as_view()),
    url(r'^produto$', views.Produto.as_view()),
    url(r'^carrinho$', views.Carrinho.as_view()),
    url(r'^cadastrar$',views.register, name='cadastrar'),
    url(r'^login$',views.auth_view, name='login'),
    url(r'^logout$',views.logout, name='logout'),
    url(r'login_compra',views.login_compra, name='login_compra'),
    url(r'^retorno/pagseguro/', include('pagseguro.urls')),
    url(r'', views.Home.as_view()),
]