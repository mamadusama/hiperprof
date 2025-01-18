from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Student
from .serializers import StudentSerializer
from teachers.models import Teacher

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
