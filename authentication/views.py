from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RegisterUserSerializer
from rest_framework import status
from django.contrib.auth import authenticate

# Create your views here.

@api_view(['POST'])
def RegisterUser(request):
    serializer = RegisterUserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({
            'email': user.email,
            'message': 'User registered successfully.'
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_framework.authtoken.models import Token
@api_view(['POST'])
def User_Login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(request, email=email, password=password)  # Ensure you have an authentication backend for email

    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)
    
    return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def User_logout(request):
    try:
        request.user.auth_token.delete()
        return Response({"message":"user logged out successfully"},status=status.HTTP_200_OK)
    except:
        return Response({"message":"error"},status=status.HTTP_200_OK)