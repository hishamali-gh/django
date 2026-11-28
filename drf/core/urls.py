# CLASS-BASED VIEWS
# GENERICAPIVIEW
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('courses', views.CourseViewSet, basename='course')

urlpatterns = [
    path('students/', views.StudentsGenericView.as_view(), name='students'),
    path('students/<int:pk>/', views.StudentGenericView.as_view(), name='student'),

    path('', include(router.urls))
]

# APIVIEW
""" from django.urls import path

from . import views

urlpatterns = [
    path('students/', views.StudentsAPIView.as_view(), name='students'),
    path('students/<int:pk>/', views.StudentAPIView.as_view(), name='student')
] """

# FUNCTTION-BASED VIEWS
""" from django.urls import path

from .views import students_view

urlpatterns = [
    path('students/', students_view, name='students'),
    path('students/<int:pk>/', students_view, name='student_details')
] """
