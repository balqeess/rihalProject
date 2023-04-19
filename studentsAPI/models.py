from django.db import models

# create the entities of our tables followed with their fields 

# Automatically generate CreatedDate and ModifiedDate properties for all entities

class Class(models.Model):
    class_name = models.CharField(max_length=50)
    createdDate = models.DateTimeField(auto_now_add=True, null=True)
    modifiedDate = models.DateTimeField(auto_now=True, null=True)

    #this method returns a string representation of an instance of the Class class
    def __str__(self):
        return self.class_name

class Country(models.Model):
    name = models.CharField(max_length=50, null=True)
    createdDate = models.DateTimeField(auto_now_add=True, null=True)
    modifiedDate = models.DateTimeField(auto_now=True, null=True)

    #this method returns a string representation of an instance of the Country class   
    def __str__(self):
        return self.name
    
class Student(models.Model):
    name = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True)
    createdDate = models.DateTimeField(auto_now_add=True, null=True)
    modifiedDate = models.DateTimeField(auto_now=True, null=True)
    #  use the 'ForeignKey' field type in the student model to define many to one relationship
    class_id = models.ForeignKey(Class, null=True, on_delete=models.SET_NULL)
    country_id = models.ForeignKey(Country, null=True,  on_delete=models.SET_NULL)

    #this method returns a string representation of an instance of the Student class
    def __str__(self):
        return self.name
   

