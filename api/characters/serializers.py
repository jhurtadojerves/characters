"""Define all serializers from Characters API"""

# Third Party Integration
from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedModelSerializer,
    HyperlinkedIdentityField,
)

# Local apps
from apps.characters.models import Character


class CharacterRelationSerializer(ModelSerializer):
    """Serializer relation from Character"""

    class Meta:
        model = Character
        fields = ("nick", "range")


class CharacterSerializer(HyperlinkedModelSerializer):
    """Serializer from character"""

    url = HyperlinkedIdentityField(
        view_name="API:characters-detail", lookup_field="slug"
    )
    lookup_field = "slug"

    class Meta:
        model = Character
        fields = (
            "url",
            "name",
            "avatar",
            "nick",
            "range",
            "is_lieutenant",
            "user",
            "characteristics",
            "job",
            "job_description",
            "patronus",
            "wand",
            "secondary_characters",
            "character_card",
            "vault",
            "storage_vault",
            "slug",
        )
