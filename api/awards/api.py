"""Define entry points"""

# Third party integration

from rest_framework import viewsets, permissions, mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin

# Local Apps
from .serializers import AwardSerializer, CategorySerializer
from apps.awards.models import Award, Category


class AwardViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    """ViewSet to Awards"""

    serializer_class = AwardSerializer
    queryset = Award.objects.all()
    lookup_field = "slug"


class CategoryViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    """ViewSet to category"""

    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = "slug"
