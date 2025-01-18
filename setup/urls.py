from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls", namespace="core")),
    path("api/teachers/", include("teachers.urls", namespace="teachers")),
    path("api/students/", include("students.urls", namespace="students")),
    path("api/auth/", include("acounts.urls", namespace="acounts")),
]
