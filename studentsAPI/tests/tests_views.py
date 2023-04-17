import datetime
from django.test import Client,TestCase
from django.urls import reverse
from studentsAPI.forms import StudentForm
from studentsAPI.models import Class, Country, Student
import json 

class StudentsStatisticsViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        # create two students for testing
        Class.objects.create(class_name='class a')
        Class.objects.create(class_name='class b')
        Country.objects.create(name='oman')
        Student.objects.create(name='balqees', date_of_birth='2001-01-01', class_id=Class.objects.get(class_name='class a'), country_id=Country.objects.get(name='oman'))
        Student.objects.create(name='ali', date_of_birth='1996-01-01', class_id=Class.objects.get(class_name='class b'), country_id=Country.objects.get(name='oman'))

    def test_students_statistics_view(self):
        response = self.client.get(reverse('students_statistics'))
        self.assertEquals(response.status_code, 200)
        # check that the expected keys are in the response context
        self.assertIn('students_count_by_class', response.context)
        self.assertIn('students_count_by_country', response.context)
        self.assertIn('avg_age', response.context)
        self.assertIn('students_statistics', response.context)

        # check that the expected data is in the response context
        expected_count_by_class = [{'class': 'class b', 'count': 1}, {'class': 'class a', 'count': 1}]
        expected_count_by_country = [{'country': 'oman', 'count': 2}]
        expected_avg_age = 24
        expected_students = Student.objects.all()

        self.assertEqual(response.context['students_count_by_class'], expected_count_by_class)
        self.assertEqual(response.context['students_count_by_country'], expected_count_by_country)
        self.assertEqual(response.context['avg_age'], expected_avg_age)
        self.assertEqual(response.context['students_statistics'].count(), expected_students.count())
        self.assertTemplateUsed(response,'studentsAPI/students_statistics.html')

    def test_get_students_form(self):
        response = self.client.get(reverse('students_insert'))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], StudentForm)
        self.assertTemplateUsed(response, 'studentsAPI/students_form.html')

    def test_get_update_students_form(self):
        # create a student object to update
        student = Student.objects.create(name='John', date_of_birth='1995-01-01', class_id=Class.objects.get(class_name='class a'), country_id=Country.objects.get(name='oman'))
        response = self.client.get(reverse('students_update', args=[student.id]))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], StudentForm)
        self.assertEqual(response.context['form'].instance, student)
        self.assertTemplateUsed(response, 'studentsAPI/students_form.html')

    def test_post_students_form_insert(self):
        form_data = {
            'name': 'Alice',
            'date_of_birth': '2000-01-01',
            'class_id': Class.objects.get(class_name='class b').id,
            'country_id': Country.objects.get(name='oman').id,
        }
        response = self.client.post(reverse('students_insert'), data=form_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('students_statistics'))
        self.assertEqual(Student.objects.count(), 3)
        new_student = Student.objects.last()
        self.assertEqual(new_student.name, 'Alice')
        self.assertEqual(str(new_student.date_of_birth), '2000-01-01')
        self.assertEqual(new_student.class_id.class_name, 'class b')
        self.assertEqual(new_student.country_id.name, 'oman')

    def test_post_students_form_update(self):
        # create a student object to update
        student = Student.objects.create(name='John', date_of_birth='1995-01-01', class_id=Class.objects.get(class_name='class a'), country_id=Country.objects.get(name='oman'))
        form_data = {
            'name': 'Alice',
            'date_of_birth': '2000-01-01',
            'class_id': Class.objects.get(class_name='class b').id,
            'country_id': Country.objects.get(name='oman').id,
        }
        response = self.client.post(reverse('students_update', args=[student.id]), data=form_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('students_statistics'))
        updated_student = Student.objects.get(pk=student.id)
        self.assertEqual(updated_student.name, 'Alice')
        self.assertEqual(str(updated_student.date_of_birth), '2000-01-01')
        self.assertEqual(updated_student.class_id.class_name, 'class b')
        self.assertEqual(updated_student.country_id.name, 'oman')