from re import search
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from django_filters import rest_framework as filters

from .serializers import CardSerializer
from .models import Card

# Create your views here.


class CardsViewSet(viewsets.ModelViewSet):

    serializer_class = CardSerializer
    queryset = Card.objects.all()
    filter_backends = (filters.DjangoFilterBackend, SearchFilter)
    filterset_fields = ('question_type',)
    search_fields = ('question',)