from django.contrib import admin
from .models import WashingtonPark, OregonPark


# Registers each model:
admin.site.register(WashingtonPark),
admin.site.register(OregonPark)
