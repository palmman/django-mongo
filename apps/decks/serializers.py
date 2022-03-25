from rest_framework import serializers
from apps.decks.models import Deck

class Deckserializer(serializers.ModelSerializer):
    
    class Meta:
        model = Deck
        fields = '__all__'