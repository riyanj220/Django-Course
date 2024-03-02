from django.db import models

class Student(models.Model):
    name=  models.CharField(max_length=100)
    age = models.IntegerField()
    email= models.EmailField()
    address  =models.TextField()
    file  =models.FileField()
    date_of_birth =models.DateField()


class Car(models.Model):
    name =models.CharField(max_length=100) 
    color =models.CharField(max_length=100)
    speed =models.IntegerField(default=100)

    def __str__(self) :
        return self.name