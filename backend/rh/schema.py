import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from .models import *

# Definicao das Types


class EmpresaType(DjangoObjectType):
    class Meta:
        model = Empresa


class FilialType(DjangoObjectType):
    class Meta:
        model = Filial


class SetorType(DjangoObjectType):
    class Meta:
        model = Setor


class CargoType(DjangoObjectType):
    class Meta:
        model = Cargo


class FuncionarioType(DjangoObjectType):
    class Meta:
        model = Funcionario


# Definicação das Querys

class Query(ObjectType):

    empresa = graphene.Field(EmpresaType, id=graphene.Int())
    empresas = graphene.List(EmpresaType)

    filial = graphene.Field(FilialType, id=graphene.Int())
    filiais = graphene.List(FilialType)

    cargo = graphene.Field(CargoType, id=graphene.Int())
    cargos = graphene.List(CargoType)

    setor = graphene.Field(SetorType, id=graphene.Int())
    setores = graphene.List(SetorType)

    funcionario = graphene.Field(FuncionarioType, id=graphene.Int())
    funcionarios = graphene.List(FuncionarioType)

    def resolve_empresa(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Empresa.objects.get(pk=id)

        return None

    def resolve_empresas(self, info, **kwargs):
        return Empresa.objects.all()

    def resolve_filial(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Filial.objects.get(pk=id)

        return None

    def resolve_filiais(self, info, **kwargs):
        return Filial.objects.all()

    def resolve_setor(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Setor.objects.get(pk=id)

        return None

    def resolve_setores(self, info, **kwargs):
        return Setor.objects.all()

    def resolve_cargo(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Cargo.objects.get(pk=id)

        return None

    def resolve_cargos(self, info, **kwargs):
        return Cargo.objects.all()

    def resolve_funcionario(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Funcionario.objects.get(pk=id)

        return None

    def resolve_funcionarios(self, info, **kwargs):
        return Funcionario.objects.all()


# Definicação dos Inputs
class EmpresaInput(graphene.InputObjectType):
    id = graphene.ID
    codigo = graphene.Int()
    descricao = graphene.String()


class FilialInput(graphene.InputObjectType):
    id = graphene.ID
    codigo = graphene.Int()
    descricao = graphene.String()
    cnpj = graphene.String()
    empresa = graphene.List(EmpresaInput)


class CargoInput(graphene.InputObjectType):
    id = graphene.ID
    codigo = graphene.Int()
    descricao = graphene.String()
    cbo = graphene.Int()


class SetorInput(graphene.InputObjectType):
    id = graphene.ID
    codigo = graphene.Int()
    descricao = graphene.String()
    empresa = graphene.List(EmpresaInput)


class FuncionarioInput(graphene.InputObjectType):
    id = graphene.ID
    matricula = graphene.Int()
    cpf = graphene.String()
    nome = graphene.String()
    filial = graphene.List(FilialInput)
    cargo = graphene.List(CargoInput)
    setor = graphene.List(SetorInput)
    data_admissao = graphene.DateTime()
    data_nascimento = graphene.DateTime()
    sexo = graphene.String()


# Mutations
class CreateEmpresa(graphene.Mutation):
    class Arguments:
        input = EmpresaInput(required=True)

    ok = graphene.Boolean()
    empresa = graphene.Field(EmpresaType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        empresa_instance = Empresa(codigo=input.codigo, descricao=input.descricao)
        empresa_instance.save()
        return CreateEmpresa(ok=ok, empresa=empresa_instance)


class UpdateEmpresa(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = EmpresaInput(required=True)

    ok = graphene.Boolean()
    empresa = graphene.Field(EmpresaType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok=False
        empresa_instance = Empresa.objects.get(pk=id)
        if empresa_instance:
            ok = True
            empresa_instance.codigo = input.codigo
            empresa_instance.descricao = input.descricao
            empresa_instance.save()
            return UpdateEmpresa(ok=ok, empresa=empresa_instance)
        return UpdateEmpresa(ok=ok, empresa=None)


class CreateFilial(graphene.Mutation):
    class Arguments:
        input = FilialInput(required=True)

    ok = graphene.Boolean()
    filial = graphene.Field(FilialType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        filiais = []
        for filial_input in input.filiais:
            filial = Filial.objects.get(pk=filial_input.id)
            if filial is None:
                return CreateFilial(ok=False, filial=None)
            filiais.append(filial)
        filial_instance = Filial(codigo=input.codigo, descricao=input.descricao, cnpj=input.cnpj)
        filial_instance.save()
        filial_instance.filiais.set(filiais)
        return CreateFilial(ok=ok, filial=filial_instance)


class UpdateFilial(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = FilialInput(required=True)

    ok = graphene.Boolean()
    filial = graphene.Field(FilialType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        filial_instance = Filial.objects.get(pk=id)
        if filial_instance:
            ok = True
            filiais = []
        for filial_input in input.filiais:
            filial = Filial.objects.get(pk=filial_input.id)
            if filial is None:
                return UpdateFilial(ok=False, filial=None)
            filiais.append(filial)
            filial_instance.title = input.title
            filial_instance.year = input.yearce.save()
            filial_instance.filiais.set(filial)
            return UpdateFilial(ok=ok, movie=filial_instance)
        return UpdateFilial(ok=ok, movie=None)


    #
    # codigo = graphene.Int()
    # descricao = graphene.String()
    # cnpj = graphene.String()
    # empresa = graphene.List(EmpresaInput)


# class UpdateFuncionario(graphene.Mutation):
#     class Arguments:
#         input = FuncionarioInput(required=True)
#     ok = graphene.Boolean()
#     funcionario = graphene.Field(FuncionarioType)
#
#     @staticmethod
#     def mutate(root, info, id, input=None):
#         ok = True
#         funcionarios = []
#         for funcionario_input in input.funcionarios:
#             funcionario = Funcionario.objects.get(pk=id)
#             if funcionario is None:
#                 return UpdateFuncionario(ok=False, funcionario=None)
#             funcionarios.append(funcionario)
#
#         funcionario_instance = Funcionario(
#             nome=input.nome
#         )


class Mutation(graphene.ObjectType):
    create_empresa = CreateEmpresa.Field()
    update_empresa = UpdateEmpresa.Field()

    create_filial = CreateFilial.Field()
    update_filial = UpdateFilial.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)