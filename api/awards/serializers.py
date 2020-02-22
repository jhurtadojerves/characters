"""Define all serializers from Characters API"""

# Third Party Integration
from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField

# Local apps
from apps.awards.models import Award, Category, Voting
from api.characters.serializers import CharacterRelationSerializer


class AwardRelationSerializer(ModelSerializer):
    """Serializer from Award in relationship"""

    class Meta:
        model = Award
        fields = ("name", "description", "slug")


class CategoryRelationSerializer(ModelSerializer):
    """Serializer from Category in relationship"""

    class Meta:
        model = Category
        fields = ("name", "description", "status")


class CategorySerializer(ModelSerializer):
    """Serializer from Category"""

    award = AwardRelationSerializer()
    participants = CharacterRelationSerializer(many=True)

    class Meta:
        model = Category
        fields = (
            "name",
            "order",
            "description",
            "max_options",
            "self_voting",
            "status",
            "award",
            "participants",
        )


class AwardSerializer(ModelSerializer):
    """Serializer from character"""

    categories = CategoryRelationSerializer(many=True, read_only=True)

    class Meta:
        model = Award
        fields = ("name", "description", "slug", "categories")
