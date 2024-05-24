from django.db import models

class Secao(models.Model):
    id_secao = models.AutoField(primary_key=True, unique=True, auto_created=True)
    cd_secao = models.CharField(max_length=1, unique=True, null=False, blank=False)
    de_secao = models.CharField(max_length=255, unique=True, null=False, blank=False)
    
    def __str__(self):
        return str(self.id_secao)
    
class Divisao(models.Model):
    id_divisao = models.AutoField(primary_key=True, unique=True, auto_created=True)
    cd_divisao = models.CharField(max_length=2, unique=True, null=False, blank=False)
    de_divisao = models.CharField(max_length=255, unique=True, null=False, blank=False)
    id_secao = models.ForeignKey(Secao, on_delete=models.PROTECT)
    
    def __str__(self):
        return str(self.id_divisao)
    
class Grupo(models.Model):
    id_grupo = models.AutoField(primary_key=True, unique=True, auto_created=True)
    cd_grupo = models.CharField(max_length=3, unique=True, null=False, blank=False)
    de_grupo = models.CharField(max_length=255, unique=True, null=False, blank=False)
    id_divisao = models.ForeignKey(Divisao, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.id_grupo)

class Classe(models.Model):
    id_classe = models.AutoField(primary_key=True, unique=True, auto_created=True)
    cd_classe = models.CharField(max_length=5, unique=True, null=False, blank=False)
    de_classe = models.CharField(max_length=255, unique=True, null=False, blank=False)
    id_grupo = models.ForeignKey(Grupo, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.id_classe)
    
class Subclasse(models.Model):
    id_subclasse = models.AutoField(primary_key=True, unique=True, auto_created=True)
    cd_subclasse = models.CharField(max_length=7, unique=True, null=False, blank=False)
    de_subclasse = models.CharField(max_length=255, unique=True, null=False, blank=False)
    id_classe = models.ForeignKey(Classe, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.id_subclasse)
    
class DivisaoSetor(models.Model):
    choices_divisao_setor = [
        (1, 'Primário'),
        (2, 'Secundário'),
        (3, 'Terciário'),
    ]

    id_divisao_setor = models.AutoField(primary_key=True, unique=True, auto_created=True)
    de_divisao_setor = models.IntegerField(choices=choices_divisao_setor, null=False, blank=False)

    def __str__(self):
        return str(self.id_divisao_setor)
    

class SetorEconomico(models.Model):
    choices_setor_economico = [
        (1, 'Comércio'),
        (2, 'Serviço'),
        (3, 'Meio Ambiente - Serviço'),
        (4, 'Indústria'),
        (5, 'Agropecuária e Pesca'),
    ]

    id_setor_economico = models.AutoField(primary_key=True, unique=True, auto_created=True)
    de_setor_economico = models.IntegerField(choices=choices_setor_economico, null=False, blank=False)

    def __str__(self):
        return str(self.id_setor_economico)
    
    
class Data(models.Model):
    choices_dt_mes = [
        (1, 'Janeiro'),
        (2, 'Fevereiro'),
        (3, 'Março'),
        (4, 'Abril'),
        (5, 'Maio'),
        (6, 'Junho'),
        (7, 'Julho'),
        (8, 'Agosto'),
        (9, 'Setembro'),
        (10, 'Outubro'),
        (11, 'Novembro'),
        (12, 'Dezembro'),
    ]

    id_data = models.AutoField(primary_key=True, unique=True, auto_created=True)
    dt_ano = models.IntegerField(null=False, blank=False, default=2020)
    dt_mes = models.IntegerField(null=False, blank=False, choices=choices_dt_mes, default=1)

    def __str__(self):
        return str(self.id_data)
    
class Arrecadacao(models.Model):
    id_arrecadacao = models.AutoField(primary_key=True, unique=True, auto_created=True)
    vl_arrecadacao = models.DecimalField(max_digits=15, decimal_places=2, null=False, blank=False)
    id_divisao_setor = models.ForeignKey(DivisaoSetor, on_delete=models.PROTECT)
    id_setor_economico = models.ForeignKey(SetorEconomico, on_delete=models.PROTECT)
    id_data = models.ForeignKey(Data, on_delete=models.PROTECT)
    id_subclasse = models.ForeignKey(Subclasse, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.id_arrecadacao)
