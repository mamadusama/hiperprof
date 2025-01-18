from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated


from .models import Teacher
from .serializers import TeacherSerializer
from .permissions import TeacherListPernission
from .serializers import TeacherProfileImageSerializer, TeacherSerializer


class TeacherList(APIView):

    permission_classes = (TeacherListPernission,)

    def get(self, request):
        q = request.query_params.get("q", "")
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
    
    def delete(self, request):
        request.user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    #TODO: Implementar a deleção de um professor mas sem excluir no banco de dados (soft delete)

class TeacherDetail(APIView):
    def get(self, request, pk):  # noqa: ARG002
        teacher = get_object_or_404(Teacher, pk=pk)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)


class MeView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        serializer = TeacherSerializer(request.user)
        return Response(serializer.data)


class TeacherProfileImageView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = TeacherProfileImageSerializer(request.user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Imagem salva com sucesso"})

    """ def put(self, request):
        teacher = request.user
        teacher.profile_image = request.data["profile_image"]
        teacher.save()
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)

    def delete(self, request):
        teacher = request.user
        teacher.profile_image = None
        teacher.save()
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)

    def get(self, request):
        teacher = request.user
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)
 """