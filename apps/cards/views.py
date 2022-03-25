from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import CardSerializer
from .models import Card

# Create your views here.


class CardsViewSet(viewsets.ModelViewSet):

    serializer_class = CardSerializer
    queryset = Card.objects.all()