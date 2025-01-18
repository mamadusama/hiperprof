from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Student
from .serializers import StudentSerializer
from teachers.models import Teacher
from rest_framework.permissions import IsAuthenticated


class StudentList(APIView):
    def post(self, request, teacher_pk):
        # Verifica se o professor existe
        teacher = get_object_or_404(Teacher, pk=teacher_pk)

        # Serializa os dados do aluno
        serializer = StudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Salva o aluno associado ao professor
        serializer.save(teacher=teacher)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


# Listagem de Estudantes de um determinado professor

class TeacherStudentList(APIView):
    
    permission_classes = (IsAuthenticated,)
    
    def get(self, request):
        
        # Verifica se o professor existe
        #teacher = get_object_or_404(Teacher, pk=teacher_pk)

        # Recupera todos os alunos associados ao professor
        students = request.user.students.all()

        # Serializa os dados dos alunos
        serializer = StudentSerializer(students, many=True)

        return Response(serializer.data)