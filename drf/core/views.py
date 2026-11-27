from rest_framework.decorators import api_view
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

        return Response(status=status.HTTP_204_NO_CONTENT)
