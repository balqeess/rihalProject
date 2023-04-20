from django.urls import path
from . import views

urlpatterns = [
    path('', views.students_form, name='students_insert'), # get and post request for insert operation
    path('delete/<int:id>/',views.students_delete,name='students_delete'),
    path('<int:id>/', views.students_form, name = 'students_update'), # get and post request for update operation
    path('list/', views.students_list, name='students_list'),
    path('statistics/', views.students_statistics, name='students_statistics') # get request to retrieve and display all statistics and data 

]
