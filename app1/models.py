from django.db import models

# Create your models here.
class Students(models.Model):
    phone = models.IntegerField(default=0)
    name = models.CharField(max_length=50)
    student_class = models.CharField(max_length=10)
    
    #class Meta:
        #verbose_name_plural = "Students"
        
class StudentDB(models.Model):
    RollNo = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100, null=False, blank=False)
    Address = models.CharField(max_length=1000, null=True, blank=True)
    Class = models.CharField(max_length=2, null=False, blank=False)
    Phone = models.IntegerField(null=True, blank=False)
    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    Gender = models.CharField(max_length=1, choices=gender_choices, null=True)
    
class Attendance(models.Model):
    RollNo = models.ForeignKey(StudentDB, db_column='RollNo', on_delete=models.DO_NOTHING)
    Date = models.CharField(max_length=10, null=False, blank=False)
    attendance_choices = [  
        ('P', 'Present'),
        ('A', 'Absent'),
    ]
    Attendance = models.CharField(max_length=1, choices=attendance_choices, null=False, blank=False)
        
