from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta: # specifies that the form should be based on the Student model 
        model = Student
        fields = ('name', 'date_of_birth', 'class_id', 'country_id')

        # to specify custom labels for the form fields.
        labels ={
            'date_of_birth': 'date of birth (yr-mm-dd)',
            'class_id': 'class',
            'country_id': 'country'
        }


    def __init__(self, *args, **kwargs): # is called when an instance of the form is created
        super(StudentForm,self).__init__(*args, **kwargs)

        # sets the empty_label(s) for the fields to "Select". 
        # This sets the default text for the select input to "Select" 
        # and ensures that the user must choose a valid option from the dropdown list.
        self.fields['class_id'].empty_label = "Select"
        self.fields['country_id'].empty_label = "Select"
