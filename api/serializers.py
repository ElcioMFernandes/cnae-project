## Serializer são responsáveis por converter os dados em um formato que pode ser facilmente consumido por um front-end, como JSON ou XML.

from rest_framework import serializers

## Precisamos importar o modelo que queremos serializar
## Geralmente, o modelo é importado do arquivo models.py

from .models import User

## Geralmente o nome do serializer é o nome do modelo seguido de "Serializer"
class UserSerializer(serializers.ModelSerializer):
    ## A classe Meta é usada para definir metadados do serializer
    class Meta:
        ## model é o modelo que será serializado
        model = User
        ## fields é uma lista com os campos que serão serializados
        fields = '__all__'
        ## '__all__' indica que todos os campos do modelo serão serializados

################################################################################

from .models import Secao, Divisao, Grupo, Classe, Subclasse

class SecaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Secao
        fields = '__all__'

class DivisaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Divisao
        fields = '__all__'

class GrupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grupo
        fields = '__all__'

class ClasseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classe
        fields = '__all__'

class SubclasseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subclasse
        fields = '__all__'