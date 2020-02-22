"""Define all routes from characters"""

# Third Party Integration
from rest_framework import routers

# Local apps
from .api import AwardViewSet, CategoryViewSet

router = routers.SimpleRouter()
router.register(r"awards", AwardViewSet)
router.register(r"categories", CategoryViewSet)
