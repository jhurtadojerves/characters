"""Define entry points"""

# Third party integration

from rest_framework import viewsets, permissions, mixins, filters
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin

# Local Apps
from .serializers import CharacterSerializer
from apps.characters.models import Character


class CharacterViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    """ViewSet to Characters"""

    serializer_class = CharacterSerializer
    queryset = Character.objects.filter(active=True)
    lookup_field = "slug"
    search_fields = ["patronus", "name", "nick", "user"]
    filter_backends = (filters.SearchFilter,)
