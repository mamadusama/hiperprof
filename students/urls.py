from django.urls import path
from .views import StudentList, TeacherStudentList

app_name = "students"

urlpatterns = [
    path(
        "professores/<str:teacher_pk>/alunos",
        StudentList.as_view(),
        name="student-list",
    ),
    path(
        "professores/alunos",
        TeacherStudentList.as_view(),
        name="teacher-student-list",
    ),
]
