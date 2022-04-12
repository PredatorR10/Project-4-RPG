from django.contrib import admin
from .models import Character, CharacterAdmin, Item, Monster, Inventory

# Register your models here.

admin.site.register(Character, CharacterAdmin)
admin.site.register(Monster)
admin.site.register(Item)
admin.site.register(Inventory)