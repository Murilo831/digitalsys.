from django.db import models

class Proposta(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    endereco = models.CharField(max_length=200)
    valor_emprestimo = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=(('Aprovado', 'Aprovado'), ('Reprovado', 'Reprovado')), default='Reprovado')


    def __str__(self):
        return self.nome

