from django.urls import path
from .views import TeacherList, TeacherDetail, MeView, TeacherProfileImageView

app_name = "teachers"

urlpatterns = [
    path("professores", TeacherList.as_view(), name="teacher-list"),
    path("professores/<uuid:pk>", TeacherDetail.as_view(), name="teacher-detail"),
    path("me", MeView.as_view(), name="me"),
    path("professores/foto", TeacherProfileImageView.as_view(), name="teacher-profile-image"),
]
