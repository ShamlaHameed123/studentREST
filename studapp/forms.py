from django.forms import ModelForm
from django import forms


from .models import Student


class StudentForm(ModelForm):
    class Meta:
        model = Student
        exclude = ('Id',)
        widgets = {
            'Date_of_birth': forms.DateInput(format=('%Y-%m-%d'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
			'DateAdded': forms.DateInput(format=('%Y-%m-%d'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
			'DateUpdated': forms.DateInput(format=('%Y-%m-%d'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }
