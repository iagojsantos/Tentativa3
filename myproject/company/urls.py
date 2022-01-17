from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from myproject.company import serializers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import CompanyListAPIViews

router = routers.DefaultRouter()

urlpatterns = [
    path('listcompany/', CompanyListAPIViews.as_view()),
    
    #path('/CreateCompany/', admin.site.urls),
    #path('/ReadCompany/', TokenObtainPairView.as_view()),
    #path('/UpdateCompany/', TokenRefreshView.as_view()),
    #path('/DeleteCompany/', ()),
    #include('rest_framework.urls', namespace='rest_framework')),
    #path(r'users/',include(router.urls)),
]