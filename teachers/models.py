from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.timezone import now
from django.db import models
import uuid

from .managers import TeacherManager

# Create your models here.


class Teacher(AbstractBaseUser, PermissionsMixin):
    id = models.CharField(
        primary_key=True,
        default=uuid.uuid4,  # Gera o UUID automaticamente
        editable=False,
        max_length=36  # Formato padrão com hífens
    )
    
    email = models.EmailField(unique=True, max_length=255)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.PositiveIntegerField(null=True)
    description = models.TextField(null=True)
    hourly_price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=now)
    # date_joined = models.DateTimeField(timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"  # This is the field that is used to log in
    REQUIRED_FIELDS = [
        "first_name",
        "last_name",
    ]  # These fields are required when creating a superuser

    objects = (
        TeacherManager()
    )  # This is the custom manager that we created in the previous step

    def __str__(self):
        return self.email
