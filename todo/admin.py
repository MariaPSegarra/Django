from django.contrib import admin
from .models import Item
# From the current directories models file we want to import the item class.

# Register your models here.
admin.site.register(Item)
