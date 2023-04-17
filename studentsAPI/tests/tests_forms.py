from django.test import TestCase
from studentsAPI.models import Class, Country
from studentsAPI.forms import StudentForm


class StudentFormTestCase(TestCase):
    def setUp(self):
        self.class_a = Class.objects.create(class_name='Class A')
        self.class_b = Class.objects.create(class_name='Class B')
        self.oman = Country.objects.create(name='Oman')
        self.kuwait = Country.objects.create(name='kuwait')

    def test_form_valid(self):
        form_data = {
            'name': 'balqees',
            'date_of_birth': '2000-01-01',
            'class_id': self.class_a.id,
            'country_id': self.oman.id,
        }
        form = StudentForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        form_data = {
            'name': '',
            'date_of_birth': '2000-01-01',
            'class_id': self.class_b.id,
            'country_id': self.kuwait.id,
        }
        form = StudentForm(data=form_data)
        self.assertFalse(form.is_valid())
