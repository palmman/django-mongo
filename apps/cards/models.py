from django.db import models
from apps.decks.models import Deck


# Create your models here.

class Card(models.Model):
    
    question = models.CharField(max_length=255)
    answer = models.TextField()
    
    class QuestionTypes(models.IntegerChoices):
        multi_choice = 1
        fill_blank = 2
        true_false = 3
        short_answer = 4
        
    question_type = models.IntegerField(choices=QuestionTypes.choices, default=4, blank=True, null=True)
    
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.question