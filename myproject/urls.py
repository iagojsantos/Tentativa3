from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from myproject.accounts import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register('user', views.UserViewSet, "usuarios")

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'users/',include(router.urls)),
]