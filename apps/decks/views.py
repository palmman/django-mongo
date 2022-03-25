from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import Deckserializer
from .models import Deck

# Create your views here.


class DecksViewSet(viewsets.ModelViewSet):

    serializer_class = Deckserializer
    queryset = Deck.objects.all()