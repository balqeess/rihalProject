from django.test import TestCase, RequestFactory
from rest_framework import status
from rest_framework.test import force_authenticate, APIRequestFactory
from studentsAPI.models import Class, Country, Student
from studentsAPI.serializers import ClassSerializer, CountrySerializer, StudentSerializer
from studentsAPI.views import ClassViewSet, CountryViewSet, StudentViewSet

class TestClassViewSet(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.view = ClassViewSet.as_view({'get': 'count_of_students_per_class'})
        self.class1 = Class.objects.create(class_name='a')
        self.student1 = Student.objects.create(name='balqees', date_of_birth='2000-01-01', class_id=self.class1)
        self.student2 = Student.objects.create(name='khadija', date_of_birth='1999-05-01', class_id=self.class1)

    def test_count_of_students_per_class(self):
        request = self.factory.get('')
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [{'class': 'a', 'count': 2}])

class TestCountryViewSet(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.view = CountryViewSet.as_view({'get': 'count_of_students_per_country'})
        self.country1 = Country.objects.create(name='KWT')
        self.student1 = Student.objects.create(name='balqees', date_of_birth='2000-01-01', country_id=self.country1)
        self.student2 = Student.objects.create(name='khadija', date_of_birth='1999-05-01', country_id=self.country1)

    def test_count_of_students_per_country(self):
        request = self.factory.get('')
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [{'country': 'KWT', 'count': 2}])

class TestStudentViewSet(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.view = StudentViewSet.as_view({'get': 'avg_age_of_students'})
        self.class1 = Class.objects.create(class_name='a')
        self.country1 = Country.objects.create(name='KWT')
        self.student1 = Student.objects.create(name='balqees', date_of_birth='2000-01-01', class_id=self.class1, country_id=self.country1)
        self.student2 = Student.objects.create(name='khadija', date_of_birth='1999-05-01', class_id=self.class1, country_id=self.country1)

    def test_avg_age_of_students(self):
        request = self.factory.get('')
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, 23)  # expected average age of students

