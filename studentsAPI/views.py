from django.shortcuts import redirect, render
from .viewsets import ClassViewSet, CountryViewSet, StudentViewSet
from .models import Student
from .forms import StudentForm

# Create your views here.
  # thru this function we return the desired display after post after redirection 
def students_statistics(request):
    # Get the data from the viewset actions
    students_count_by_class = ClassViewSet.as_view({'get': 'count_of_students_per_class'})(request).data
    students_count_by_country = CountryViewSet.as_view({'get': 'count_of_students_per_country'})(request).data
    avg_age = int(StudentViewSet.as_view({'get': 'avg_age_of_students'})(request).data)
    context = {
        'students_count_by_class': students_count_by_class,
        'students_count_by_country': students_count_by_country,
        'avg_age': avg_age,
        'students_statistics': Student.objects.all()
    }
    return render(request,"studentsAPI/students_statistics.html",context)

def students_form(request):# if insert operation we have not provided id the id will be zero
    if request.method == "GET":
        form = StudentForm()
        return render(request,"studentsAPI/students_form.html", {'form':form})
    else:
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/student/statistics')
#def students_form(request, id=0):# if insert operation we have not provided id the id will be zero
    if request.method == "GET": #GET REQUEST
        if id==0: # we will have insert operation
            form = StudentForm()
        else: # if it is an update operation
            student = Student.objects.get(pk=id)
            form = StudentForm(instance=student)
        return render(request, "studentsAPI/students_form.html", {'form': form})
    else:# POST OPERATION WILL BE HANDLED HERE 
        if id == 0: #INSERT
            form = StudentForm(request.POST)
        else: #UPADTE
            student = Student.objects.get(pk=id)
            form = StudentForm(request.POST, instance = student) #the first paraemter passes the info from the form
            # the 2nd parameter we have the employee object which has the data from the DB which is to be updated with 
            #the first parameter
        
        if form.is_valid():# this is for both insert and update operations
            form.save()
            #after the save operation we will redirect the user into the route for showing the record 
            # all inserted users so far
        return redirect('/student/statistics')
        

    

def students_delete(request,id):
    student = Student.objects.get(pk=id)
    student.delete()
    return redirect('/student/statistics')

    
