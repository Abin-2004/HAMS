from django.db import models

# Create your models here.
class DepartmentDb(models.Model):
    Department_Name = models.CharField(max_length=100)
    Department_Description = models.TextField()
    Department_Image = models.ImageField(upload_to="department/",blank=True, null=True)

    def __str__(self):
        return self.Department_Name
class DoctorDb(models.Model):
    Doctor_Name = models.CharField(max_length=100)
    Department = models.CharField(max_length=100)
    Email = models.EmailField()
    Phone = models.IntegerField()
    Qualification = models.CharField(max_length=200)
    Experience = models.IntegerField()
    Image = models.ImageField(upload_to="doctor/",blank=True, null=True)

    def __str__(self):
        return self.Doctor_Name
