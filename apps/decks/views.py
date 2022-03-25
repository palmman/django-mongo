from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import Deckserializer
from .models import Deck
from apps.cards.serializers import CardSerializer
from apps.cards.models import Card

# Create your views here.


class DecksViewSet(viewsets.ModelViewSet):

    serializer_class = Deckserializer
    queryset = Deck.objects.all()
    
class DeckCardViewSet(viewsets.ModelViewSet):
    
    serializer_class = CardSerializer
    queryset = Card.objects.all()
    
    def list(self, request, decks_pk):
        cards = Card.objects.filter(deck=decks_pk)
        serializer = self.get_serializer(cards, many=True)
        return Response(serializer.data)
        