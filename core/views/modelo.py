from rest_framework.viewsets import ModelViewSet

from core.models import Modelo
from core.serializers import ModeloSerializer

class ModeloViewSet(ModelViewSet):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer