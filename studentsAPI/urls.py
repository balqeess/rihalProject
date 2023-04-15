from django.urls import path
from . import views

urlpatterns = [
    path('', views.students_form),
    path('statistics/', views.students_statistics)

]
