"""Define all urls from API"""


# Third Party Integration
from .patches import routers  # Extended Rest Framework Routers

# Local
from .awards.router import router as awards
from .characters.router import router as characters

router = routers.DefaultRouter()

router.extend(awards)
router.extend(characters)

urlpatterns = router.urls
