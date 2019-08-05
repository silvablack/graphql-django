from django.contrib import admin
from .models import *


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    pass


@admin.register(Setor)
class SetorAdmin(admin.ModelAdmin):
    pass


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    pass


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    pass


@admin.register(Filial)
class FilialAdmin(admin.ModelAdmin):
    pass
