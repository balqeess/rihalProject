'''from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from studentsAPI.models import Student,Class,Country
import json 

class TestCountryViewSet(TestCase):
    def setUp(self):
        self.client = APIClient()
        # create test data for the Country and Student models here
        Country.objects.create(name='Oman')
        Country.objects.create(name='United Arab Emirates')
        Class.objects.create(class_name='Class A')
        Class.objects.create(class_name='Class B')
        Student.objects.create(name='Jane', date_of_birth='1997-09-23', class_id=Class.objects.get(class_name='Class B'), country_id=Country.objects.get(name='Oman'))
        Student.objects.create(name='Ali', date_of_birth='2000-01-01', class_id=Class.objects.get(class_name='Class A'), country_id=Country.objects.get(name='Oman'))
        Student.objects.create(name='Ahmed', date_of_birth='2000-01-01', class_id=Class.objects.get(class_name='Class A'), country_id=Country.objects.get(name='United Arab Emirates'))

    def test_count_of_students_per_class_action(self):
        response = self.client.get(reverse('students_statistics'))

        # check that the response status code is 200
        self.assertEqual(response.status_code, 200)

        # check that the expected data is in the response data
        expected_data = [
            {'class': 'Class A', 'count': 2},
            {'class': 'Class B', 'count': 1}
        ]
        self.assertEqual(response.data, expected_data)

    def test_count_of_students_per_country_action(self):
        response = self.client.get(reverse('students_statistics'))

        # check that the response status code is 200
        self.assertEqual(response.status_code, 200)

        # check that the expected data is in the response data
        expected_data = [{'country': 'Oman', 'count': 2}, {'country': 'United Arab Emirates', 'count': 1}]
        self.assertEqual(response.data, expected_data)

    def test_avg_age_of_students_action(self):
        response = self.client.get(reverse('students_statistics'))

        # check that the response status code is 200
        self.assertEqual(response.status_code, 200)

        # check that the expected data is in the response data
        expected_data = 22  # replace with the expected average age based on your test data
        self.assertEqual(response.data, expected_data)'''
