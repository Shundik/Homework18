from .Students import SStudents
from django.forms import ModelForm


class StudentsForm(ModelForm):

    class Meta:
        model = SStudents
        fields = ['first_name', 'second_name']

