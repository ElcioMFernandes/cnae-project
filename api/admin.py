from django.contrib import admin

from .models import Secao, Divisao, Grupo, Classe, Subclasse, DivisaoSetor, SetorEconomico, Data, Arrecadacao

class SecaoAdmin(admin.ModelAdmin):
    list_display = ('id_secao', 'cd_secao', 'de_secao')

class DivisaoAdmin(admin.ModelAdmin):
    list_display = ('id_divisao', 'cd_divisao', 'de_divisao', 'id_secao')

class GrupoAdmin(admin.ModelAdmin):
    list_display = ('id_grupo', 'cd_grupo', 'de_grupo', 'id_divisao')

class ClasseAdmin(admin.ModelAdmin):
    list_display = ('id_classe', 'cd_classe', 'de_classe', 'id_grupo')

class SubclasseAdmin(admin.ModelAdmin):
    list_display = ('id_subclasse', 'cd_subclasse', 'de_subclasse', 'id_classe')

class DivisaoSetorAdmin(admin.ModelAdmin):
    list_display = ('id_divisao_setor', 'de_divisao_setor')

class SetorEconomicoAdmin(admin.ModelAdmin):
    list_display = ('id_setor_economico', 'de_setor_economico')

class DataAdmin(admin.ModelAdmin):
    list_display = ('id_data', 'dt_ano', 'dt_mes')

class ArrecadacaoAdmin(admin.ModelAdmin):
    list_display = ('id_arrecadacao', 'id_data', 'id_subclasse', 'id_setor_economico', 'vl_arrecadacao', 'id_divisao_setor')
    
admin.site.register(Secao, SecaoAdmin)
admin.site.register(Divisao, DivisaoAdmin)
admin.site.register(Grupo, GrupoAdmin)
admin.site.register(Classe, ClasseAdmin)
admin.site.register(Subclasse, SubclasseAdmin)
admin.site.register(DivisaoSetor, DivisaoSetorAdmin)
admin.site.register(SetorEconomico, SetorEconomicoAdmin)
admin.site.register(Data, DataAdmin)
admin.site.register(Arrecadacao, ArrecadacaoAdmin)