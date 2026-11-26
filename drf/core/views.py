from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def students_view(request):
    if request.method == 'GET':
        return Response({'students': ['Hisham', 'Rinsha']})

    if request.method == 'POST':
        print(request.POST, request.body, request.data)
