from django.shortcuts import render
from rest_framework import viewsets
from myproject.company.models import Company
from .serializers import  CompanySerializer 
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics

from myproject.company import serializers


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer 
    permission_classes = [IsAuthenticated]

    def  post(self, request, format = None): #metodo get é de retorno
        content = {
            'user': str(request.user),
            'auth': str(request.auth),
        }
        return Response(content)

class CompanyListAPIViews(generics.ListAPIView):
     queryset = Company.objects.all()
     serializer_class = CompanySerializer
     #permission_classes = [IsAuthenticated]

