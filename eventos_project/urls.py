from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from eventos_app import views


router = DefaultRouter()
router.register(r'eventos', views.EventoViewSet)
router.register(r'participantes', views.ParticipanteViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', views.home, name='home'),
]