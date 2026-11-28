# CLASS-BASED VIEWS
# GENERICAPIVIEW
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import filters

from django_filters.rest_framework import DjangoFilterBackend

from .models import Student
from .serializers import StudentModelSerializer

class StudentsGenericView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

    filter_backends = [filters.OrderingFilter, filters.SearchFilter, DjangoFilterBackend]

    ordering_fields = ['name', 'age']  # Fields the clients are allowed to sort by.
    ordering = ['name']  # The default ordering field if none is specified.

    search_fields = ['name', 'email']  # Fields 'SearchFilter will look across (case-insensitive).

    # filterset_fields = ['name', 'age', 'email']  # Exact fields 'django-filters' searches

    # Using django-filter with specified lookups:
    filterset_fields = {
        'name': ['iexact', 'icontains'],  # Enables (only) 'name__iexact' and 'name__icontains' in the search bar!
        'age': ['exact', 'gte', 'lte'],  # Enables 'age=...', 'age__gte', and 'age__lte'.
        'email': ['iexact']  # Enables 'email__iexact'.
    }

class StudentGenericView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

# APIVIEW
""" from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404

from .serializers import StudentModelSerializer
from .models import Student

class StudentsAPIView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentModelSerializer(students, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = StudentModelSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        student = serializer.save()

        return Response({'message': f'{student.name} is created'}, status=status.HTTP_201_CREATED)

class StudentAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Student, pk=pk)

    def get(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentModelSerializer(student)

        return Response(serializer.data)

    def put(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentModelSerializer(student, data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response({'message': f'{student.name} is updated (PUT)'})

    def patch(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentModelSerializer(student, data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response({'message': f'{student.name} is updated (PUT)'})

    def delete(self, request, pk):
        student = self.get_object(pk)

        student.delete()

        return Response(status=status.HTTP_204_NO_CONTENT) """

# FUNCTION-BASED VIEWS
""" from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404

from .serializers import StudentModelSerializer
from .models import Student

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def students_view(request, pk=None):
    if pk:
        student = get_object_or_404(Student, pk=pk)

    else:
        students = Student.objects.all()

    if request.method == 'GET':
        if pk:
            serializer = StudentModelSerializer(student)

            return Response(serializer.data)

        serializer = StudentModelSerializer(students, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StudentModelSerializer(data=request.data)

        if serializer.is_valid():
            student = serializer.save()

            return Response({'message': f'{student.name} created'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        serializer = StudentModelSerializer(student, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({'message': f'{student.name} has updated (PUT)'})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        serializer = StudentModelSerializer(student, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response({'message': f'{student.name} has updated (PATCH)'})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()

        return Response(status=status.HTTP_204_NO_CONTENT) """
