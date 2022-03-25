from xml.etree.ElementInclude import include
from rest_framework import routers
from .views import DecksViewSet
from django.urls import path, include

from rest_framework_nested import routers
from .views import DeckCardViewSet


router = routers.SimpleRouter()
router.register(r'', DecksViewSet)

card_router = routers.NestedSimpleRouter(router,'', lookup='decks')
card_router.register('cards', DeckCardViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(card_router.urls)),
]