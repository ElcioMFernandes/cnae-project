## URLs são rotas que o Django utiliza para redirecionar o usuário para as páginas corretas.
from django.contrib import admin
from django.urls import path, include
## No caso da nossa api precisamos importar o router e a view que criamos.
from rest_framework import routers
import api.views as views

## Aqui criamos um objeto router que vai ser responsável por criar as rotas da nossa API.
router = routers.DefaultRouter()
## Aqui registramos a rota para o nosso UserViewSet.
router.register(r'users', views.UserViewSet)
router.register(r'secoes', views.SecaoViewSet)
router.register(r'divisoes', views.DivisaoViewSet)
router.register(r'grupos', views.GrupoViewSet)
router.register(r'classes', views.ClasseViewSet)
router.register(r'subclasses', views.SubclasseViewSet)

## Aqui criamos as rotas da nossa API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('secoes/<str:cd_secao>/divisoes/', views.DivisaoSecao.as_view()),
    path('divisoes/<str:cd_divisao>/grupos/', views.GrupoDivisao.as_view()),
    path('grupos/<str:cd_grupo>/classes/', views.ClasseGrupo.as_view()),
    path('classes/<str:cd_classe>/subclasses/', views.SubclasseClasse.as_view()),
]
