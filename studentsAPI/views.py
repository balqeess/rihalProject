from django.shortcuts import redirect, render
from .viewsets import ClassViewSet, CountryViewSet, StudentViewSet
from .models import Student
from .forms import StudentForm


def students_statistics(request):

    # using .as_view method the function creates instances of the viewsets 
    # passing in a dictionary that maps the HTTP method to the name of the custom action.

    students_count_by_class = ClassViewSet.as_view({'get': 'count_of_students_per_class'})(request).data
    students_count_by_country = CountryViewSet.as_view({'get': 'count_of_students_per_country'})(request).data
    avg_age = StudentViewSet.as_view({'get': 'avg_age_of_students'})(request).data

    # it stores the retrieved statistics in a dictionary, which is then passed to the template when it is rendered. 
    context = {
        'students_count_by_class': students_count_by_class,
        'students_count_by_country': students_count_by_country,
        'avg_age': avg_age,
    }

    # it renders the studentsAPI/students_statistics.html template using the render() function and returns the rendered template as an HTTP response.
    return render(request,"studentsAPI/students_statistics.html",context)

def students_list(request):
    context = {'students_list': Student.objects.all()}
    return render(request, "studentsAPI/students_list.html",context)


def students_form(request, id=0):# if insert operation we have not provided id the id will be zero
    if request.method == "GET": #GET REQUEST
        if id==0: # we will have insert operation

            # creates an instance of the StudentForm form class and passes it to the 'students_form.html'
            form = StudentForm() 

        else: # if it is an update operation

            student = Student.objects.get(pk=id) # retrieves the student record with the corresponding id from the database

            # populates an instance of the StudentForm form class with the data, and passes it to the template.
            form = StudentForm(instance=student) 

        return render(request, "studentsAPI/students_form.html", {'form': form})
    
    else:# POST OPERATION WILL BE HANDLED HERE 

        if id == 0: #INSERT

            #creates an instance of the StudentForm form class with the request data
            # The request.POST parameter is a dictionary-like object that contains the submitted form data.
            form = StudentForm(request.POST)

        else: #UPADTE

            student = Student.objects.get(pk=id)
            form = StudentForm(request.POST, instance = student) #the first parameter passes the info from the form
            # the 2nd parameter we have the student object which has the data from the DB which is to be updated with 
            #the first parameter
        
    
        # performs various validation checks on the submitted data,
        # such as checking that required fields are present,
        #  and that the data is in the correct format.
        if form.is_valid():# this is for both insert and update operations

            form.save() # saves the data to the database

            #after the save operation we will redirect the user into the route for showing the records of
            # all inserted users so far
        return redirect('students_statistics')
        

    

def students_delete(request,id):

    #retrieves the Student object from the database based on the given ID 
    student = Student.objects.get(pk=id)
    student.delete()

    # redirects the user to the students_statistics route, 
    # which will display a list of all the remaining students after the deletion.
    return redirect('students_statistics')






    
