from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from myproject.accounts import views

router = routers.DefaultRouter()
router.register('user', views.UserViewSet, "usuarios")

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'users/',include(router.urls)),
]