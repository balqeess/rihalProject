from django.urls import path
from . import views

urlpatterns = [
    path('', views.students_form, name='students_insert'),
    path('delete/<int:id>/',views.students_delete,name='students_delete'),
    path('<int:id>/', views.students_form, name = 'students_update'), # get and post req for update operation
    path('statistics/', views.students_statistics, name='students_statistics')

]
