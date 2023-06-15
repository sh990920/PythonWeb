from django import forms
from .models import Show

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Show
        fields = ("showTitle", "showCategory", "showPeriod", "showPlace", "ticketPrice")