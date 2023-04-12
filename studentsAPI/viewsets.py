from rest_framework import viewsets
from .serializers import ClassSerializer, CountrySerializer, StudentSerializer
from .models import Class, Country, Student
from django.db.models import Count, Avg
from rest_framework.decorators import action
from rest_framework.response import Response

''' a ViewSet is a class-based view that provides CRUD (Create, Retrieve, Update, Delete) functionality for a model or a queryset. 
'''

class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer

    @action(detail=False, methods=['get'])
    def count_of_students_per_class(self, request):
        students_count_by_class = Student.objects.values('class_id').annotate(count=Count('id'))
        data = [{'Class': item['class_id'], 'count': item['count']} for item in students_count_by_class]
        return Response(data)



class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    @action(detail=False, methods=['get'])
    def count_of_students_per_country(self, request):
        students_count_by_country = Student.objects.values('country_id').annotate(count=Count('id'))
        data = [{'Country': item['country_id'], 'count': item['count']} for item in students_count_by_country]
        return Response(data)

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class =  StudentSerializer

    @action(detail=False, methods=['get'])
    def avg_age_of_students(self, request):
        avg_age = Student.objects.aggregate(avg_age=Avg('age'))
        return Response(avg_age)
