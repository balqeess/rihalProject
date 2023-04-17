from django.test import Client, TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from unittest.mock import patch

class TestClassViewSet(TestCase):
    def setUp(self):
        self.client = APIClient()
        # create test data for the Class model here

    def test_count_of_students_per_class_action(self):
        response = self.client.get(reverse('class-count-of-students-per-class'))

        # check that the response status code is 200
        self.assertEqual(response.status_code, 200)

        # check that the expected data is in the response data
        # replace the expected data with your own test data
        expected_data = [{'class': 'Class A', 'count': 5}, {'class': 'Class B', 'count': 7}]
        self.assertEqual(response.data, expected_data)

class TestCountryViewSet(TestCase):
    def setUp(self):
        self.client = APIClient()
        # create test data for the Country model here

    def test_count_of_students_per_country_action(self):
        response = self.client.get(reverse('country-count-of-students-per-country'))

        # check that the response status code is 200
        self.assertEqual(response.status_code, 200)

        # check that the expected data is in the response data
        # replace the expected data with your own test data
        expected_data = [{'country': 'USA', 'count': 10}, {'country': 'Canada', 'count': 2}]
        self.assertEqual(response.data, expected_data)

class TestStudentViewSet(TestCase):
    def setUp(self):
        self.client = APIClient()
        # create test data for the Student model here

    def test_avg_age_of_students_action(self):
        response = self.client.get(reverse('student-avg-age-of-students'))

        # check that the response status code is 200
        self.assertEqual(response.status_code, 200)

        # check that the expected data is in the
