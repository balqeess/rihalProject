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

    # to retrieve all instances of the Class model from the database.
    queryset = Class.objects.all()

    # specifies the serializer class that should be used to serialize and deserialize instances of the Class model.
    serializer_class = ClassSerializer

    @action(detail=False, methods=['get'])
    def count_of_students_per_class(self, request):

        # The values() method is used to group the results by the class_id__class_name attribute of the Student model
        # The annotate() method is used to add a count attribute to the resulting QuerySet, which specifies the number of students in each class.
        students_count_by_class = Student.objects.values('class_id__class_name').annotate(count=Count('id'))

        #list of dictionaries, where each dictionary represents a class and its corresponding student count, 
        # and returns this data as a JSON response using the Django Rest Framework's Response class.
        data = [{'class': item['class_id__class_name'], 'count': item['count']} for item in students_count_by_class]
        return Response(data)



class CountryViewSet(viewsets.ModelViewSet):

    # retrieve all instances of the Country model from the database.
    queryset = Country.objects.all()
     # specifies the serializer class that should be used to serialize and deserialize instances of the Country model.
    serializer_class = CountrySerializer

    @action(detail=False, methods=['get'])
    def count_of_students_per_country(self, request):

        # The values() method is used to group the results by the country_id__name attribute of the Country model
        # The annotate() method is used to add a count attribute to the resulting QuerySet, which specifies the number of students in each country.
        students_count_by_country = Student.objects.values('country_id__name').annotate(count=Count('id'))

        #list of dictionaries, where each dictionary represents a country and its corresponding student count, 
        # and returns this data as a JSON response using the Django Rest Framework's Response class.
        data = [{'country': item['country_id__name'], 'count': item['count']} for item in students_count_by_country]
        return Response(data)

class StudentViewSet(viewsets.ModelViewSet):

    # to retrieve all instances of the Student model from the database.
    queryset = Student.objects.all()

    # specifies the serializer class that should be used to serialize and deserialize instances of the Student model.
    serializer_class =  StudentSerializer

    @action(detail=False, methods=['get'])

    def avg_age_of_students(self, request):
        students = Student.objects.all()
        total_age = 0
        if students:
            for student in students:
                age = (date.today() - student.date_of_birth).days / 365.25 # converting days to years
                total_age += age # adds up the ages of all students
            avg_age = total_age / len(students)  # divides the total by the number of students to get the average age.
        else:
            avg_age = 0  #If there are no students in the database, the method returns an average age o
        
      #returns the average age as an integer value wrapped in a JSON response using the Django Rest Framework's Response class.
        return Response(int(avg_age))
