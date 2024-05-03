## As views são responsáveis por receber as requisições HTTP e retornar as respostas HTTP.
from rest_framework import viewsets, generics, response, permissions, status

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

from .models import Secao, Divisao, Grupo, Classe, Subclasse, DivisaoSetor, SetorEconomico, Data, Arrecadacao
from .serializers import SecaoSerializer, DivisaoSerializer, GrupoSerializer, ClasseSerializer, SubclasseSerializer, DivisaoSecaoSerializer, GrupoDivisaoSerializer, ClasseGrupoSerializer, SubclasseClasseSerializer, DivisaoSetorSerializer, SetorEconomicoSerializer, DataSerializer, ArrecadacaoSerializer

class SecaoViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]

    queryset = Secao.objects.all()
    serializer_class = SecaoSerializer
    lookup_field = 'cd_secao'

    def get_object(self):
        self.kwargs[self.lookup_field] = self.kwargs.get(self.lookup_field, "").upper()
        return super().get_object()

    def create(self, request, *args, **kwargs):
        return response.Response({"error": "POST requests not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, *args, **kwargs):
        return response.Response({"error": "PUT requests not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, *args, **kwargs):
        return response.Response({"error": "DELETE requests not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

class DivisaoViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]

    queryset = Divisao.objects.all()
    serializer_class = DivisaoSerializer
    lookup_field = 'cd_divisao'

    def create(self, request, *args, **kwargs):
        return response.Response({"error": "POST requests not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, *args, **kwargs):
        return response.Response({"error": "PUT requests not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, *args, **kwargs):
        return response.Response({"error": "DELETE requests not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

class GrupoViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]

    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer
    lookup_field = 'cd_grupo'

    def create(self, request, *args, **kwargs):
        return response.Response({"error": "POST requests not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, *args, **kwargs):
        return response.Response({"error": "PUT requests not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, *args, **kwargs):
        return response.Response({"error": "DELETE requests not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

class ClasseViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]

    queryset = Classe.objects.all()
    serializer_class = ClasseSerializer
    lookup_field = 'cd_classe'

    def create(self, request, *args, **kwargs):
        return response.Response({"error": "POST requests not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, *args, **kwargs):
        return response.Response({"error": "PUT requests not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, *args, **kwargs):
        return response.Response({"error": "DELETE requests not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

class SubclasseViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]

    queryset = Subclasse.objects.all()
    serializer_class = SubclasseSerializer
    lookup_field = 'cd_subclasse'

    def create(self, request, *args, **kwargs):
        return response.Response({"error": "POST requests not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, *args, **kwargs):
        return response.Response({"error": "PUT requests not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, *args, **kwargs):
        return response.Response({"error": "DELETE requests not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

class DivisaoSetorViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    
    queryset = DivisaoSetor.objects.all()
    serializer_class = DivisaoSetorSerializer

    def create(self, request, *args, **kwargs):
        return response.Response({"error": "POST requests not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, *args, **kwargs):
        return response.Response({"error": "PUT requests not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, *args, **kwargs):
        return response.Response({"error": "DELETE requests not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

class SetorEconomicoViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    
    queryset = SetorEconomico.objects.all()
    serializer_class = SetorEconomicoSerializer

    def create(self, request, *args, **kwargs):
        return response.Response({"error": "POST requests not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, *args, **kwargs):
        return response.Response({"error": "PUT requests not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, *args, **kwargs):
        return response.Response({"error": "DELETE requests not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

class DataViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]

    queryset = Data.objects.all()
    serializer_class = DataSerializer

    def create(self, request, *args, **kwargs):
        return response.Response({"error": "POST requests not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, *args, **kwargs):
        return response.Response({"error": "PUT requests not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, *args, **kwargs):
        return response.Response({"error": "DELETE requests not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

class ArrecadacaoViewSet(viewsets.ModelViewSet):

    queryset = Arrecadacao.objects.all()
    serializer_class = ArrecadacaoSerializer

class DivisaoSecao(generics.ListAPIView):
    def get_queryset(self):
        queryset = Divisao.objects.filter(id_secao__cd_secao=self.kwargs['cd_secao'].upper())
        return queryset
    serializer_class = DivisaoSecaoSerializer

class GrupoDivisao(generics.ListAPIView):
    def get_queryset(self):
        queryset = Grupo.objects.filter(id_divisao__cd_divisao=self.kwargs['cd_divisao'])
        return queryset
    serializer_class = GrupoDivisaoSerializer

class ClasseGrupo(generics.ListAPIView):
    def get_queryset(self):
        queryset = Classe.objects.filter(id_grupo__cd_grupo=self.kwargs['cd_grupo'])
        return queryset
    serializer_class = ClasseGrupoSerializer

class SubclasseClasse(generics.ListAPIView):
    def get_queryset(self):
        queryset = Subclasse.objects.filter(id_classe__cd_classe=self.kwargs['cd_classe'])
        return queryset
    serializer_class = SubclasseClasseSerializer