from django.db import models
class student(models.Model):
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=50)
    email = models.EmailField()
    roll_no=models.CharField(max_length=10)
    mobile_no=models.CharField(max_length=10)
    def __str__(self):
        return self.name
