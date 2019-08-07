from django.db import models
from datetime import date


class Empresa(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.BigIntegerField()
    descricao = models.CharField(max_length=50)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return str(self.codigo) + " - " + str(self.descricao)

    class Meta:
        ordering = ('descricao', )


class Filial(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.BigIntegerField()
    descricao = models.CharField(max_length=50)
    cnpj = models.BigIntegerField()
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.codigo) + " - " + str(self.descricao)

    class Meta:
        ordering = ('descricao', )


class Cargo(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.BigIntegerField()
    descricao = models.CharField(max_length=50)
    cbo = models.BigIntegerField()

    def __str__(self):
        return str(self.id) + " - " + str(self.descricao)

    class Meta:
        ordering = ('descricao', )


class Setor(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.BigIntegerField()
    descricao = models.CharField(max_length=50)
    empresa = models.ForeignKey(Empresa, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + " - " + str(self.codigo) + " - " + str(self.descricao)

    class Meta:
        ordering = ('descricao', )


def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


class Funcionario(models.Model):
    id = models.AutoField(primary_key=True)
    matricula = models.BigIntegerField()
    cpf = models.CharField(max_length=11, unique=True)
    nome = models.CharField(max_length=50)
    filial = models.ForeignKey(Filial, on_delete=models.CASCADE)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)
    data_admissao = models.DateField()
    data_nascimento = models.DateField()
    sexo = models.CharField(max_length=1)

    @property
    def idade(self):
        return calculate_age(self.data_nascimento)

    class Meta:
        ordering = ('nome', )
