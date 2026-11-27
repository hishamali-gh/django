from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import StudentSerializer
from .models import Student

@api_view(['GET', 'POST'])
def students_view(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)

        return Response(serializer.data)

    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            student = serializer.save()

            return Response({'message': f'{student.name} created'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
