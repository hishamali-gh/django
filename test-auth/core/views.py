from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from rest_framework import status

from .serializers import SignUpSerializer, LoginSerializer

class SignUpView(APIView):
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

            return Response(
                {'message': 'User registered successfully', 'username': user.username},
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class LoginView(APIView):
#     def post(self, request):
#         serializer = LoginSerializer(data=request.data)

#         if serializer.is_valid():
#             return Response(
#                 {'message': 'User logged in successfully', 'username': serializer.validated_data.get('username')},
#                 status=status.HTTP_200_OK
#             )

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(
            {
                'message': f'Hello, {request.user.username}! You are authenticated with Basic Authentication.',
                'user_id': request.user.id
            },

            status=status.HTTP_200_OK
        )
