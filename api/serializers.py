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

from .models import Secao, Divisao, Grupo, Classe, Subclasse, DivisaoSetor, SetorEconomico, Data, Arrecadacao

class SecaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Secao
        exclude = ['id_secao']

class DivisaoSerializer(serializers.ModelSerializer):
    cd_secao = serializers.CharField(source='id_secao.cd_secao')
    de_secao = serializers.CharField(source='id_secao.de_secao')
    
    class Meta:
        model = Divisao
        fields = ['cd_divisao', 'de_divisao', 'cd_secao', 'de_secao']

class GrupoSerializer(serializers.ModelSerializer):
    cd_divisao = serializers.CharField(source='id_divisao.cd_divisao')
    de_divisao = serializers.CharField(source='id_divisao.de_divisao')
    cd_secao = serializers.CharField(source='id_divisao.id_secao.cd_secao')
    de_secao = serializers.CharField(source='id_divisao.id_secao.de_secao')

    class Meta:
        model = Grupo
        fields = ['cd_grupo', 'de_grupo', 'cd_divisao', 'de_divisao', 'cd_secao', 'de_secao']

class ClasseSerializer(serializers.ModelSerializer):
    cd_grupo = serializers.CharField(source='id_grupo.cd_grupo')
    de_grupo = serializers.CharField(source='id_grupo.de_grupo')
    cd_divisao = serializers.CharField(source='id_grupo.id_divisao.cd_divisao')
    de_divisao = serializers.CharField(source='id_grupo.id_divisao.de_divisao')
    cd_secao = serializers.CharField(source='id_grupo.id_divisao.id_secao.cd_secao')
    de_secao = serializers.CharField(source='id_grupo.id_divisao.id_secao.de_secao')

    class Meta:
        model = Classe
        fields = ['cd_classe', 'de_classe', 'cd_grupo', 'de_grupo', 'cd_divisao', 'de_divisao', 'cd_secao', 'de_secao']    

class SubclasseSerializer(serializers.ModelSerializer):
    cd_classe = serializers.CharField(source='id_classe.cd_classe')
    de_classe = serializers.CharField(source='id_classe.de_classe')
    cd_grupo = serializers.CharField(source='id_classe.id_grupo.cd_grupo')
    de_grupo = serializers.CharField(source='id_classe.id_grupo.de_grupo')
    cd_divisao = serializers.CharField(source='id_classe.id_grupo.id_divisao.cd_divisao')
    de_divisao = serializers.CharField(source='id_classe.id_grupo.id_divisao.de_divisao')
    cd_secao = serializers.CharField(source='id_classe.id_grupo.id_divisao.id_secao.cd_secao')
    de_secao = serializers.CharField(source='id_classe.id_grupo.id_divisao.id_secao.de_secao')

    class Meta:
        model = Subclasse
        fields = ['cd_subclasse', 'de_subclasse', 'cd_classe', 'de_classe', 'cd_grupo', 'de_grupo', 'cd_divisao', 'de_divisao', 'cd_secao', 'de_secao']

class DivisaoSetorSerializer(serializers.ModelSerializer):
    de_divisao_setor = serializers.CharField(source='get_de_divisao_setor_display', read_only=True)

    class Meta:
        model = DivisaoSetor
        fields = '__all__'

class SetorEconomicoSerializer(serializers.ModelSerializer):
    de_setor_economico = serializers.CharField(source='get_de_setor_economico_display', read_only=True)

    class Meta:
        model = SetorEconomico
        fields = '__all__'

class DataSerializer(serializers.ModelSerializer):
    dt_mes = serializers.CharField(source='get_dt_mes_display', read_only=True)

    class Meta:
        model = Data
        fields = '__all__'

class ArrecadacaoSerializer(serializers.ModelSerializer):
    vl_arrecadacao = serializers.FloatField()
    cd_subclasse = serializers.CharField(source='id_subclasse.cd_subclasse')
    de_subclasse = serializers.CharField(source='id_subclasse.de_subclasse')
    cd_classe = serializers.CharField(source='id_subclasse.id_classe.cd_classe')
    de_classe = serializers.CharField(source='id_subclasse.id_classe.de_classe')
    cd_grupo = serializers.CharField(source='id_subclasse.id_classe.id_grupo.cd_grupo')
    de_grupo = serializers.CharField(source='id_subclasse.id_classe.id_grupo.de_grupo')
    cd_divisao = serializers.CharField(source='id_subclasse.id_classe.id_grupo.id_divisao.cd_divisao')
    de_divisao = serializers.CharField(source='id_subclasse.id_classe.id_grupo.id_divisao.de_divisao')
    cd_secao = serializers.CharField(source='id_subclasse.id_classe.id_grupo.id_divisao.id_secao.cd_secao')
    de_secao = serializers.CharField(source='id_subclasse.id_classe.id_grupo.id_divisao.id_secao.de_secao')
    de_setor_economico = serializers.SerializerMethodField()
    de_divisao_setor = serializers.SerializerMethodField()
    dt_mes = serializers.SerializerMethodField()
    
    class Meta:
        model = Arrecadacao
        fields = [
            'id_arrecadacao',
            'vl_arrecadacao',
            'cd_secao',
            'de_secao',
            'cd_divisao',
            'de_divisao',
            'cd_grupo',
            'de_grupo',
            'cd_classe',
            'de_classe',
            'cd_subclasse',
            'de_subclasse',
            'dt_mes',
            'de_setor_economico',
            'de_divisao_setor'
            ]
        
    def get_dt_mes(self, obj):
        return obj.id_data.get_dt_mes_display()
    
    def get_de_setor_economico(self, obj):
        return obj.id_setor_economico.get_de_setor_economico_display()
    
    def get_de_divisao_setor(self, obj):
        return obj.id_divisao_setor.get_de_divisao_setor_display()

class DivisaoSecaoSerializer(serializers.ModelSerializer):
    cd_secao = serializers.CharField(source='id_secao.cd_secao')

    class Meta:
        model = Divisao
        fields = ['cd_secao', 'cd_divisao', 'de_divisao']

    def create(self, validated_data):
        cd_secao = validated_data.pop('id_secao')['cd_secao']
        secao = Secao.objects.get(cd_secao=cd_secao)
        divisao = Divisao.objects.create(id_secao=secao, **validated_data)
        return divisao
        
class GrupoDivisaoSerializer(serializers.ModelSerializer):
    cd_divisao = serializers.CharField(source='id_divisao.cd_divisao')

    class Meta:
        model = Grupo
        fields = ['cd_divisao', 'cd_grupo', 'de_grupo']

    def create(self, validated_data):
        cd_divisao = validated_data.pop('id_divisao')['cd_divisao']
        divisao = Divisao.objects.get(cd_divisao=cd_divisao)
        grupo = Grupo.objects.create(id_divisao=divisao, **validated_data)
        return grupo
    
class ClasseGrupoSerializer(serializers.ModelSerializer):
    cd_grupo = serializers.CharField(source='id_grupo.cd_grupo')

    class Meta:
        model = Classe
        fields = ['cd_grupo', 'cd_classe', 'de_classe']

    def create(self, validated_data):
        cd_grupo = validated_data.pop('id_grupo')['cd_grupo']
        grupo = Grupo.objects.get(cd_grupo=cd_grupo)
        classe = Classe.objects.create(id_grupo=grupo, **validated_data)
        return classe
    
class SubclasseClasseSerializer(serializers.ModelSerializer):
    cd_classe = serializers.CharField(source='id_classe.cd_classe')

    class Meta:
        model = Subclasse
        fields = ['cd_classe', 'cd_subclasse', 'de_subclasse']

    def create(self, validated_data):
        cd_classe = validated_data.pop('id_classe')['cd_classe']
        classe = Classe.objects.get(cd_classe=cd_classe)
        subclasse = Subclasse.objects.create(id_classe=classe, **validated_data)
        return subclasse
