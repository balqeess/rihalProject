# we use serializers for the conversion of the dataflow that are usually
# complex data types such as querysets and models instances (in python representaion in this case)
#  to a format that can be easily rendered into JSON, XML.

from rest_framework import serializers
from .models import Class, Country, Student

class ClassSerializer(serializers.ModelSerializer):

    class Meta:
        model = Class
        fields = '__all__'

class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = '__all__'

class Studenterializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__' 


