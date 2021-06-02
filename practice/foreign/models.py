from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Doctor(models.Model):
    doc_id =models.CharField(primary_key='True',max_length=100)
    name = models.CharField(max_length=200)

    def __str__(self) :
        return self.name

class Medical(models.Model):
    Doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    mediacal_id = models.CharField(primary_key='True', max_length=50)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Patient(models.Model):
    doc_id = models.ForeignKey(Doctor, on_delete=models.CASCADE, default=1)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    email   = models.EmailField(max_length=100)
    name = models.CharField(max_length=200)
    def __str__(self) :
        return self.name




