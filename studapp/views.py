from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
# Create your views here.
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import StudentSerializer
from .models import Student


class StudentCreateApi(APIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentApi(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Student.objects.all()
        context={"data":list(queryset.values())}
        print(context)
        return Response(context)




class StudentUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDeleteApi(generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
