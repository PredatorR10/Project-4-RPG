from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CLASS_CHOICES = (
    ("war", "Warrior"),
    ("arc", "Archer"),
    ("mag", "Mage")
)

class Character(models.Model):
    name = models.CharField(max_length=50)
    charClass = models.CharField(max_length=20, choices = CLASS_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']