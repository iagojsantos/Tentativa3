from myproject.accounts.models import User
from myproject.accounts.models import Client
from rest_framework import serializers

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User, Client
        fields = ["name", "cpf", "email", "status", "address",]