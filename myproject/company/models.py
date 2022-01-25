from django.db import models
from myproject.accounts.models import User
from django.conf import settings
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

def upload_file_customer(instance, filename):
    return f'{instance.name}-{filename}'

class Company(models.Model):
    managers = models.ManyToManyField(User, related_name='company', blank = True) #verbose_name='Gerente' )
    name = models.CharField(("Nome"), max_length=30) #verbose_name= 'Nome'#)
    cnpj = models.CharField(('CNPJ'), max_length=18, blank=True, null=True)
    email = models.EmailField(max_length=50)
    status = models.CharField(max_length=30)
    address = models.CharField(('Endereço'),max_length=90) #verbose_name='Endereço')
    city = models.CharField(('Cidade'), max_length=30)# verbose_name='Cidade')

    class Meta:
        verbose_name_plural = 'Company'
    def __str__(self):
        return self.name     


      
