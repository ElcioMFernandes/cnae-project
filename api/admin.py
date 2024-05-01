## No admin do Django, podemos ver as tabelas do banco de dados e manipulá-las.
from django.contrib import admin
## Aqui importamos o modelo User que criamos.
from .models import User

## Aqui registramos o modelo User para que ele apareça no admin.
class UserAdmin(admin.ModelAdmin):
    ## Listamos os campos que queremos que apareçam na tabela do admin.
    list_display = ('id_user', 'name', 'email', 'created_at', 'updated_at')

################################################################################

from .models import Secao, Divisao, Grupo, Classe, Subclasse

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

## Aqui registramos o modelo User e a classe UserAdmin.
admin.site.register(User, UserAdmin)
admin.site.register(Secao, SecaoAdmin)
admin.site.register(Divisao, DivisaoAdmin)
admin.site.register(Grupo, GrupoAdmin)
admin.site.register(Classe, ClasseAdmin)
admin.site.register(Subclasse, SubclasseAdmin)
