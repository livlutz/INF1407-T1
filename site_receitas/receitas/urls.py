
from django.contrib import admin
from django.urls import path
from receitas import views

app_name = 'receitas'

urlpatterns = [
    path('', views.PubReceitasListView.as_view(), name = 'homepage'),
    path('receita/<int:id>/', views.VerReceita.as_view(), name = 'ver_receita'),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)