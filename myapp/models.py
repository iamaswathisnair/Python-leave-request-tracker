from django.db import models

choice=(('waiting','waiting'),('approved','approved'),('rejected','rejected'),)


# Create your models here.


class Employe(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=7)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    birth = models.DateField()
    designation = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.first_name

class leave(models.Model):
    name=models.CharField(max_length=100)
    date=models.DateField()
    type=models.CharField(max_length=100)
    reason=models.CharField(max_length=100)
    reason=models.CharField(max_length=100)
    status=models.CharField(max_length=10,choices=choice)
   
    def __str__(self):
        return self.type
   

class complaint(models.Model):
    name=models.CharField(max_length=200)
    date=models.DateField()
    designation=models.CharField(max_length=100)
    reason=models.CharField(max_length=100)

    def __str__(self):
        return self. reason