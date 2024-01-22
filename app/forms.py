from django import forms
from .models import Todolist

class DateInput(forms.DateInput):
    input_type = 'date'

class Addproject(forms.ModelForm):

    class Meta:
        model = Todolist
        fields = ['title', 'description', 'deadline']

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control', 'id':'titleid'}),
            'description':forms.TextInput(attrs={'class':'form-control', 'id':'descriptionid'}),
            'deadline': DateInput(attrs={'class':'form-control', 'id':'deadlineid'}),  
        }

        