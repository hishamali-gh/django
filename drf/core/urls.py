# CLASS-BASED VIEWS
# APIVIEW
from django.urls import path

from . import views

urlpatterns = [
    path('students/', views.StudentsAPIView.as_view(), name='students'),
    path('students/<int:pk>/', views.StudentAPIView.as_view(), name='student')
]

# FUNCTTION-BASED VIEWS
""" from django.urls import path

from .views import students_view

urlpatterns = [
    path('students/', students_view, name='students'),
    path('students/<int:pk>/', students_view, name='student_details')
] """
