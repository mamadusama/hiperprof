from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated



from .models import Teacher
from .serializers import TeacherSerializer
from .permissions import TeacherListPernission


class TeacherList(APIView):
    
    permission_classes = (TeacherListPernission,)
    
    def get(self, request):
        q = request.query_params.get('q', '')
        teachers = Teacher.objects.filter(description__icontains=q)
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def put(self, request):
        serializer = TeacherSerializer(request.user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
        

class TeacherDetail(APIView):
    def get(self, request, pk): # noqa: ARG002
        teacher = get_object_or_404(Teacher, pk=pk)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)


class MeView(APIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request):
        serializer = TeacherSerializer(request.user)
        return Response(serializer.data)