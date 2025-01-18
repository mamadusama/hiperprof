from django.db import models
import uuid




class Student(models.Model):
    id = models.CharField(
        primary_key=True,
        default=uuid.uuid4,  # Gera o UUID automaticamente
        editable=False,
        max_length=36  # Formato padrão com hífens
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    clas_date = models.DateField()
    teacher = models.ForeignKey('teachers.Teacher', on_delete=models.CASCADE, related_name='students')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"
