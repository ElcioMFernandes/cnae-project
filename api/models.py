## Models são classes que representam tabelas no banco de dados. Cada atributo da classe representa uma coluna na tabela.

from django.db import models

## Para criar um modelo, você deve criar uma classe que herda de models.Model
class User(models.Model):
    ## Cada atributo da classe representa uma coluna na tabela
    id_user = models.AutoField(primary_key=True, unique=True, auto_created=True)
    ## primary_key=True indica que esse campo é a chave primária da tabela
    ## unique=True indica que esse campo não pode ter valores duplicados
    ## auto_created=True indica que esse campo é auto incrementado

    name = models.CharField(max_length=100)
    ## max_length é o tamanho máximo do campo

    email = models.EmailField(unique=True)
    ## EmailField é um campo específico para armazenar e-mails

    password = models.CharField(max_length=100)
    ## CharField é um campo de texto

    created_at = models.DateTimeField(auto_now_add=True)
    ## auto_now_add=True indica que o campo é preenchido automaticamente com a data e hora atuais quando um registro é criado

    updated_at = models.DateTimeField(auto_now=True)
    ## auto_now=True indica que o campo é preenchido automaticamente com a data e hora atuais sempre que um registro é atualizado

    ## O método __str__ é chamado quando você tenta imprimir um objeto do modelo
    ## Nesse caso, ele retornará o valor do atributo name
    def __str__(self):
        return self.name

################################################################################

## Seção     A         Agricultura, pecuária, produção fl orestal, pesca e aqüicultura
## Divisão   01        Agricultura, pecuária e serviços relacionados
## Grupo     01.1      Produção de lavouras temporárias
## Classe    01.11-3   Cultivo de cereais
## Subclasse 0111-3/01 Cultivo de arroz

class Secao(models.Model):
    id_secao = models.AutoField(primary_key=True, unique=True, auto_created=True) # Identificador único da seção
    cd_secao = models.CharField(max_length=1, unique=True, null=False, blank=False) # Código da seção
    de_secao = models.CharField(max_length=255, unique=True, null=False, blank=False) # Descrição da seção
    
    def __str__(self):
        return str(self.id_secao)
    
class Divisao(models.Model):
    id_divisao = models.AutoField(primary_key=True, unique=True, auto_created=True) # Identificador único da divisão
    cd_divisao = models.CharField(max_length=2, unique=True, null=False, blank=False) # Código da divisão
    de_divisao = models.CharField(max_length=255, unique=True, null=False, blank=False) # Descrição da divisão
    id_secao = models.ForeignKey(Secao, on_delete=models.PROTECT) # Chave estrangeira para a seção
    
    def __str__(self):
        return str(self.id_divisao)
    
class Grupo(models.Model):
    id_grupo = models.AutoField(primary_key=True, unique=True, auto_created=True) # Identificador único do grupo
    cd_grupo = models.CharField(max_length=3, unique=True, null=False, blank=False) # Código do grupo
    de_grupo = models.CharField(max_length=255, unique=True, null=False, blank=False) # Descrição do grupo
    id_divisao = models.ForeignKey(Divisao, on_delete=models.PROTECT) # Chave estrangeira para a divisão

    def __str__(self):
        return str(self.id_grupo)

class Classe(models.Model):
    id_classe = models.AutoField(primary_key=True, unique=True, auto_created=True) # Identificador único da classe
    cd_classe = models.CharField(max_length=5, unique=True, null=False, blank=False) # Código da classe
    de_classe = models.CharField(max_length=255, unique=True, null=False, blank=False) # Descrição da classe
    id_grupo = models.ForeignKey(Grupo, on_delete=models.PROTECT) # Chave estrangeira para o grupo

    def __str__(self):
        return str(self.id_classe)
    
class Subclasse(models.Model):
    id_subclasse = models.AutoField(primary_key=True, unique=True, auto_created=True) # Identificador único da subclasse
    cd_subclasse = models.CharField(max_length=7, unique=True, null=False, blank=False) # Código da subclasse
    de_subclasse = models.CharField(max_length=255, unique=True, null=False, blank=False) # Descrição da subclasse
    id_classe = models.ForeignKey(Classe, on_delete=models.PROTECT) # Chave estrangeira para a classe

    def __str__(self):
        return str(self.id_subclasse)