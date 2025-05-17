from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from .views import hospitais_list, ComentarioViewSet, comentarios_por_hospital

# Personalização do painel admin
admin.site.site_header = 'Administração do Conexão Hospitalar'
admin.site.site_title = 'Administração do Conexão Hospitalar'
admin.site.index_title = ''

# Roteador para viewsets (comentários em geral)
router = DefaultRouter()
router.register(r'comentarios', ComentarioViewSet)

urlpatterns = [
    # Listagem de todos os hospitais
    path('hospitais/', hospitais_list, name='hospitais_list'),

    # Comentários de um hospital específico (GET aberto, POST exige login)
    path('hospitais/<int:hospital_id>/comentarios/', comentarios_por_hospital, name='comentarios_por_hospital'),

    # Autenticação: login, logout, verificação, etc.
    path('auth/', include('dj_rest_auth.urls')),

    # Registro de usuários
    path('auth/registration/', include('dj_rest_auth.registration.urls')),

    # Comentários gerais (via viewset REST: GET, POST, PUT, DELETE)
    path('', include(router.urls)),
]
