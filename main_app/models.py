from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CLASS_CHOICES = (
    ("Warrior", "Warrior"),
    ("Archer", "Archer"),
    ("Mage", "Mage")
)

class Character(models.Model):
    name = models.CharField(max_length=50)
    charClass = models.CharField(max_length=20, choices = CLASS_CHOICES)
    level = models.IntegerField(default=1)
    exp = models.IntegerField(default=0)
    expReq = models.IntegerField(default=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def addExp(self, gain):
        self.exp += gain
        if self.exp >= self.expReq:
            self.exp -= self.expReq
            self.expReq += 500
            self.level += 1
        return self.exp

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['level']

class Monster(models.Model):
    name = models.CharField(max_length=50)
    level = models.IntegerField()
    health = models.IntegerField()
    mana = models.IntegerField()
    expYield = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['level']