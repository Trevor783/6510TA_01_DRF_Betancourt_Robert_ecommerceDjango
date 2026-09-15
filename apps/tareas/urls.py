from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TareaViewSet, CategoriaViewSet

router = DefaultRouter()
router.register(r'tareas', TareaViewSet, basename='tarea')
router.register(r'categorias', CategoriaViewSet, basename='categoria')

urlpatterns = [
    path('', include(router.urls)),
]

