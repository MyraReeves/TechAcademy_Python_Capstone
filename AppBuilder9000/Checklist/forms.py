from django.forms import ModelForm
from .models import WashingtonPark


# Convert all fields of "WashingtonPark" content into HTML:
class ParkForm (ModelForm):
    class Meta:
        model = WashingtonPark
        fields = '__all__'
