from django.urls import path
from .views import addStudent,editStudent, deleteStudent, StudentApi
from django.conf.urls import url



urlpatterns = [
    path('api/list', StudentApi.as_view(), name="Student-list"),
    path('api/create',addStudent, name="add-Student"),
    path('api/<int:Id>',editStudent, name="edit-Student"),
    path('api/<int:Id>/delete',deleteStudent, name="delete-Student"),
]
