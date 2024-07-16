from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny,DjangoModelPermissions



class RecipeView(ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    filterset_fields = ['category','ingredients']
    search_fields = ['name']

class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class IngredientView(ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    



@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    password = request.data.get('password')
    hash_password = make_password(password)
    request.data['password']= hash_password
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response('User Created!')
    else:
        return Response(serializer.errors)
    
@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = authenticate(username=email, password= password)

    if user == None:
        return Response('Email or password is invalid', status=status.HTTP_400_BAD_REQUEST)
    else:
        token,_ = Token.objects.get_or_create(user=user) 
        return Response(token.key)
    