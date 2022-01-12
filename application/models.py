from django.db import models

class Employee(models.Model):
    name=models.TextField()
    email=models.EmailField()
    phone=models.IntegerField()
    address=models.TextField()
    city=models.TextField()
    zipcode=models.IntegerField()
    
    class Meta:
        db_table="employee"
    
