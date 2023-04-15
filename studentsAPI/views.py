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
    avg_age = StudentViewSet.as_view({'get': 'avg_age_of_students'})(request).data
    context = {
        'students_count_by_class': students_count_by_class,
        'students_count_by_country': students_count_by_country,
        'avg_age': avg_age,
        'students_list': Student.objects.all()
    }
    return render(request,"studentsAPI/students_statistics.html",context)

def students_form(request):
    if request.method == "GET": #GET REQUEST
        form = StudentForm()
        return render(request,"studentsAPI/students_form.html", {'form':form})
    else: # if it is an update operation
            form = StudentForm(request.POST)
            if form.is_valid():
                 form.save()
            return redirect('/student/statistics')
        
    

def students_delete(request):
    return
