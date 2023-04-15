from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.students_form),
    path('statistics/', views.students_statistics)

]
