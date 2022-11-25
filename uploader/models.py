from django.db import models

# Create your models here.
class Cat(models.Model):
    name=models.CharField(max_length=30)
    picture=models.FileField(upload_to='media/')
