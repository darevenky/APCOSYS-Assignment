from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Details(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,unique=True)
    address = models.TextField()
    cell_no = models.CharField(max_length=10)
    is_access = models.CharField(max_length=3,default='yes')
    role = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

    
    