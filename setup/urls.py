## URLs são rotas que o Django utiliza para redirecionar o usuário para as páginas corretas.
from django.contrib import admin
from django.urls import path, include
## No caso da nossa api precisamos importar o router e a view que criamos.
from rest_framework import routers
from api.views import UserViewSet, SecaoViewSet, DivisaoViewSet, GrupoViewSet, ClasseViewSet, SubclasseViewSet

## Aqui criamos um objeto router que vai ser responsável por criar as rotas da nossa API.
router = routers.DefaultRouter()
## Aqui registramos a rota para o nosso UserViewSet.
router.register(r'users', UserViewSet)
router.register(r'secoes', SecaoViewSet)
router.register(r'divisoes', DivisaoViewSet)
router.register(r'grupos', GrupoViewSet)
router.register(r'classes', ClasseViewSet)
router.register(r'subclasses', SubclasseViewSet)

## Aqui criamos as rotas da nossa API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
