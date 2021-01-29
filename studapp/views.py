from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
# Create your views here.
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import StudentSerializer
from .models import Student
from .forms import StudentForm


class StudentCreateApi(APIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentApi(APIView):
    def get(self, request, *args, **kwargs):
        draw = int(request.GET.get('draw', 0))
        length = int(request.GET.get('length', 25))
        start = int(request.GET.get('start', 0))
        querysets = Student.objects.all()
        total = querysets.count()

        queryset = querysets[start:start+length]
        context={"data":list(queryset.values()), "recordsTotal":total, "recordsFiltered": total}
        return Response(context)


def addStudent(request):
    if request.method == "POST":
	    form = StudentForm(request.POST)
	    if form.is_valid():
		    # print("aaaaa")
		    try:
			    form.instance.user = request.user
			    form.save()
			    # print("bbbbbbbb")
			    model = form.instance
			    return redirect('http://localhost:8001/home')
		    except Exception as e:
			    print(e)
			    print(form.errors)
			    pass
    else:
	    form = StudentForm()
    return render(request, 'create.html', {'form': form})


def editStudent(request, Id):
    student = Student.objects.get(Id=Id)
    form = StudentForm(initial={'First_name': student.First_name,
                             'Last_name': student.Last_name,
                             'Date_of_birth': student.Date_of_birth,
                             'Email': student.Email,
							 'Class_level': student.Class_level,
							 'Phone_number': student.Phone_number,
							 'Parent_name': student.Parent_name,
							 'DateAdded': student.DateAdded,
							 'DateUpdated': student.DateUpdated,
                             'Year_joined': student.Year_joined})
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('http://localhost:8001/home')
            except Exception as e:
                pass
    return render(request, 'edit.html', {'form': form})


def deleteStudent(request, Id):
    student = Student.objects.get(Id=Id)
    try:
        student.delete()
    except Exception as e:
        pass
    return redirect('http://localhost:8001/home')
