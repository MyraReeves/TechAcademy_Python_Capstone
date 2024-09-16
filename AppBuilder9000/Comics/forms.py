from django.forms import ModelForm
from .models import ComicbookCollection


# Creates a class object named ComicbookForm, inheriting from the class ModelForm:
class ComicbookForm(ModelForm):
    class Meta:
        model = ComicbookCollection
        fields = '__all__'
