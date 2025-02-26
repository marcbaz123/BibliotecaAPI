from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter
from .api import BookViewSet, CopiesViewSet, EditorialsViewSet


# Ruta predeterminada de book 
router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')
router.register(r'editorials', EditorialsViewSet, basename='editorials')
# Ruta anidada para acceder a las copias de un libro específico
books_router = NestedDefaultRouter(router, r'books', lookup='book')
books_router.register(r'copies', CopiesViewSet, basename='copies')

urlpatterns = [
    path('', include(router.urls)),
    # Incluye las rutas anidadas de copias
    path('', include(books_router.urls)),
]
