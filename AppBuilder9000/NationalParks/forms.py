from django.forms import ModelForm
from .models import VisitorComment


# Creates a form class object named CommentForm (inheriting from ModelForm)
# to convert "VisitorComment" content into HTML:
class CommentForm(ModelForm):
    class Meta:
        # Creates a variable to hold the class "VisitorComment":
        model = VisitorComment

        # Chooses all the "VisitorComment" fields (park name, weather, etc.) using the "all" dunder:
        fields = '__all__'
