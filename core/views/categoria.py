from rest_framework.viewsets import ModelViewSet

from core.models import Categoria, Categoria
from core.serializers import CategoriaSerializer, CategoriaSerializer

...
class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer