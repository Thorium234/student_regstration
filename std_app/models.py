from django.db import models

# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    reg_number=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=100,null=True)
    email_address=models.EmailField(max_length=244 )
    created=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return (f'{self.first_name} {self.last_name}')
