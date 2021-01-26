from django.urls import path
from .views import StudentCreateApi, StudentApi, StudentUpdateApi, StudentDeleteApi



urlpatterns = [
    path('api/',StudentApi.as_view()),
    path('api/create',StudentCreateApi.as_view()),
    path('api/<int:pk>',StudentUpdateApi.as_view()),
    path('api/<int:pk>/delete',StudentDeleteApi.as_view()),
]
