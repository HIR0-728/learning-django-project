from django.forms import ModelForm
from placticeapp.models import Person


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = (
            "first_name",
            "last_name",
            "age",
            "nickname",
        )
