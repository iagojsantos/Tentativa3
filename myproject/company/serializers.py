from myproject.accounts.models import User
from rest_framework import serializers

from myproject.company.models import Company

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = [ "cnpj", "status", "address", "city"]