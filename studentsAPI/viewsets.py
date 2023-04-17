from rest_framework import viewsets
from .serializers import ClassSerializer, CountrySerializer, StudentSerializer
from .models import Class, Country, Student
from django.db.models import Count, Avg
from rest_framework.decorators import action
from rest_framework.response import Response
from datetime import date

''' a ViewSet is a class-based view that provides CRUD (Create, Retrieve, Update, Delete) functionality for a model or a queryset. 
'''

class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer

    @action(detail=False, methods=['get'])
    def count_of_students_per_class(self, request):
        students_count_by_class = Student.objects.values('class_id__class_name').annotate(count=Count('id'))
        data = [{'class': item['class_id__class_name'], 'count': item['count']} for item in students_count_by_class]
        return Response(data)



class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    @action(detail=False, methods=['get'])
    def count_of_students_per_country(self, request):
        students_count_by_country = Student.objects.values('country_id__name').annotate(count=Count('id'))
        data = [{'country': item['country_id__name'], 'count': item['count']} for item in students_count_by_country]
        return Response(data)

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class =  StudentSerializer

    @action(detail=False, methods=['get'])
    def avg_age_of_students(self, request):
        students = Student.objects.all()
        total_age = 0
        if students:
            for student in students:
                age = (date.today() - student.date_of_birth).days / 365 # converting days to years
                total_age += age
            avg_age = total_age / len(students) 
        else:
            avg_age = 0
        return Response(avg_age)
