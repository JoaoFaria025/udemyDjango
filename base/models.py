from django.db import models

class Cliente(models.Model):
    nome = models.CharField('Nome',max_length=80)
    sobrenome = models.CharField('Nome', max_length=80)
    email = models.EmailField('Digite seu email')

    def _str_(self):
        return self.nome
