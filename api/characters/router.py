"""Define all routes from characters"""

# Third Party Integration
from rest_framework import routers

# Local apps
from .api import CharacterViewSet

router = routers.SimpleRouter()
router.register(r"characters", CharacterViewSet)
