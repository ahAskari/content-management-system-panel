from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    avatar = models.ImageField(blank=True, null=True, upload_to='media/avatar')
    ROLES = (
        ('admin', 'Admin'),
        ('editor', 'Editor'),
        ('viewer', 'Viewer'),
    )
    role = models.CharField(max_length=20, choices=ROLES, default='viewer')


    def __str__(self):
        return f'{self.pk} - {self.role} - {self.username}'