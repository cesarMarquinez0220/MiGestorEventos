from django.urls import path
from . import views

urlpatterns = [
    path('', views.EventoListView.as_view(), name='lista_eventos'),
    path('crear/', views.EventoCreateView.as_view(), name='crear_evento'),
    path('editar/<int:pk>/', views.EventoUpdateView.as_view(), name='editar_evento'),
    path('organizadores/', views.OrganizadorListView.as_view(), name='lista_organizadores'),
    path('organizadores/crear/', views.OrganizadorCreateView.as_view(), name='crear_organizador'),
]
