from django.test import TestCase
from datetime import date
from studentsAPI.models import Class, Country, Student

# Setting up the environment for the tests by creating instances of Class, Country, and Student

class TestModels(TestCase):

    def setUp(self):
        self.class_a = Class.objects.create(class_name='Class A')
        self.country_oman = Country.objects.create(name='Oman')
        self.student_1 = Student.objects.create(name='balqees', date_of_birth=date(2001, 8, 8), class_id=self.class_a, country_id=self.country_oman)
        self.student_2 = Student.objects.create(name='ali', date_of_birth=date(2001, 5, 5), class_id=self.class_a, country_id=self.country_oman)

    def test_class_string_representation(self):
        self.assertEqual(str(self.class_a), 'Class A')

    def test_country_string_representation(self):
        self.assertEqual(str(self.country_oman), 'Oman')

    def test_student_string_representation(self):
        self.assertEqual(str(self.student_1), 'balqees')
        self.assertEqual(str(self.student_2), 'ali')

    def test_student_class_relationship(self):
        self.assertEqual(self.student_1.class_id, self.class_a)
        self.assertEqual(self.student_2.class_id, self.class_a)

    def test_student_country_relationship(self):
        self.assertEqual(self.student_1.country_id, self.country_oman)
        self.assertEqual(self.student_2.country_id, self.country_oman)

    def test_student_date_of_birth(self):
        self.assertEqual(self.student_1.date_of_birth, date(2001, 8, 8))
        self.assertEqual(self.student_2.date_of_birth, date(2001, 5, 5))

