## As views são responsáveis por receber as requisições HTTP e retornar as respostas HTTP.
from rest_framework import viewsets

## Precisamos importar o modelo e o serializer que queremos usar na view
from .models import User
from .serializers import UserSerializer

## O nome da classe geralmente é o nome do modelo seguido de "ViewSet"
class UserViewSet(viewsets.ModelViewSet):
    ## queryset é a lista de objetos que será retornada na resposta
    queryset = User.objects.all() 
    ## serializer_class é o serializer que será usado para serializar os dados
    serializer_class = UserSerializer

################################################################################

from .models import Secao, Divisao, Grupo, Classe, Subclasse
from .serializers import SecaoSerializer, DivisaoSerializer, GrupoSerializer, ClasseSerializer, SubclasseSerializer

class SecaoViewSet(viewsets.ModelViewSet):
    queryset = Secao.objects.all()
    serializer_class = SecaoSerializer

class DivisaoViewSet(viewsets.ModelViewSet):
    queryset = Divisao.objects.all()
    serializer_class = DivisaoSerializer

class GrupoViewSet(viewsets.ModelViewSet):
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer

class ClasseViewSet(viewsets.ModelViewSet):
    queryset = Classe.objects.all()
    serializer_class = ClasseSerializer

class SubclasseViewSet(viewsets.ModelViewSet):
    queryset = Subclasse.objects.all()
    serializer_class = SubclasseSerializer