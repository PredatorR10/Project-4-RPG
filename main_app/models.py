from operator import truediv
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

# Create your models here.

CLASS_CHOICES = (
    ("Warrior", "Warrior"),
    ("Archer", "Archer"),
    ("Mage", "Mage")
)

SLOT_CHOICES = (
    ("Armor", "Armor"),
    ("Weapon", "Weapon")
)

class Item(models.Model):
    name = models.CharField(max_length=50)
    equipable = models.BooleanField(default=False)
    equipSlot = models.CharField(max_length=20, choices = SLOT_CHOICES)
    statHealth = models.IntegerField(blank=True, null=True)
    statAttack = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


class Character(models.Model):
    name = models.CharField(max_length=50)
    charClass = models.CharField(max_length=20, choices = CLASS_CHOICES)
    level = models.IntegerField(default=1)
    health = models.IntegerField(default=100)
    mana = models.IntegerField(default=50)
    attack = models.IntegerField(default=7)
    exp = models.IntegerField(default=0)
    expReq = models.IntegerField(default=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    inv = models.ManyToManyField(
        Item,
        through='Inventory',
        through_fields=('character', 'item')
    )

    def equip(self, item):
        for each in self.inventory_set.all():
            if each.item.name == item:
                slot = each.item.equipSlot
                for gear in self.inventory_set.all():
                    if gear.item.equipSlot == slot and gear.equiped == True:
                        self.unequip(gear.item.name)
                        print(gear.item.name)
                each.equiped = True
                if(each.item.statHealth):
                    self.health += each.item.statHealth
                if(each.item.statAttack):
                    self.attack += each.item.statAttack
                self.save()
                each.save()
                return

    def unequip(self, item):
        for each in self.inventory_set.all():
            if each.item.name == item:
                each.equiped = False
                if(each.item.statHealth):
                    self.health -= each.item.statHealth
                if(each.item.statAttack):
                    self.attack -= each.item.statAttack
                self.save()
                each.save()
                return

    def addExp(self, gain):
        self.exp += gain
        if self.exp >= self.expReq:
            self.exp -= self.expReq
            self.expReq += 500
            self.level += 1
            self.health += 20
            self.mana += 10
            self.attack += 3
        return self.exp

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-level']

class Inventory(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)
    equiped = models.BooleanField(default=False)

    def __str__(self):
        return (self.character.name+":"+self.item.name)

class InventoryInline(admin.TabularInline):
    model = Inventory
    extra = 1

class CharacterAdmin(admin.ModelAdmin):
    inlines = (InventoryInline, )

class Monster(models.Model):
    name = models.CharField(max_length=50)
    level = models.IntegerField()
    health = models.IntegerField()
    mana = models.IntegerField()
    attack = models.IntegerField()
    expYield = models.IntegerField()
    drops = models.ManyToManyField(Item)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['level']