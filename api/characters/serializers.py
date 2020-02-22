"""Define all serializers from Characters API"""

# Third Party Integration
from rest_framework.serializers import ModelSerializer

# Local apps
from apps.characters.models import Character


class CharacterRelationSerializer(ModelSerializer):
    """Serializer relation from Character"""

    class Meta:
        model = Character
        fields = ("nick", "range")


class CharacterSerializer(ModelSerializer):
    """Serializer from character"""

    class Meta:
        model = Character
        fields = (
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
            "business",
            "slug",
        )
