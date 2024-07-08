from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from pastagem import views as views_pastagem
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path(':676700/admin', admin.site.urls),
    path('', views_pastagem.index, name='index'),
    path('calculo/', views_pastagem.calculo, name='calculo'),
    #path('pastagens_calculadas/<int:pk>/', views_pastagem.pastagens_calculadas, name='pastagens_calculadas'),

]

# Configuração para redirecionar todas as URLs não encontradas para a página inicial
urlpatterns += [
    path('<path:not_found>/', RedirectView.as_view(url='/', permanent=False)),
]
