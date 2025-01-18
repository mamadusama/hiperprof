from django.urls import path
from .views import StudentList

app_name = 'students'

urlpatterns = [
    path('professores/<str:teacher_pk>/alunos', StudentList.as_view(), name='student-list'),
]
