from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    rool_no = models.CharField(max_length=50)
    age = models.IntegerField()
    
    def __str__(self) -> str:
        return self.name
    
class Teacher(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.name
    
class Uploads(models.Model):
    uploaded_file = models.FileField(upload_to="File_Uploads/", max_length=100)
    model_name = models.CharField(max_length=50)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.model_name