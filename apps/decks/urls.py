from rest_framework import routers
from .views import DecksViewSet

router = routers.SimpleRouter()
router.register(r'', DecksViewSet)
urlpatterns = router.urls