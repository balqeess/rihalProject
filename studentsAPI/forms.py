from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'date_of_birth', 'class_id', 'country_id')
        labels ={
            'date_of_birth': 'date of birth',
            'class_id': 'class',
            'country_id': 'country'
        }


    def __init__(self, *args, **kwargs):
        super(StudentForm,self).__init__(*args, **kwargs)
        self.fields['class_id'].empty_label = "Select"
        self.fields['country_id'].empty_label = "Select"
