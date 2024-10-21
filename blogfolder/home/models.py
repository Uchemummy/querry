# from django.db import models

# # Create your models here.
# from django.db import models

# # Create your models here.


# student_types = [
#     ('leader', 'cohort leader'),
#      ('deputy', 'vice leader'),
#     ('secretary', 'secretary'),
#     ('President', 'President'),
#      ('member', 'member'),

# ]
# class Student(models.Model):
#     username = models.CharField(max_length=100, unique=True)
#     first_name = models.CharField(max_length=200, null=True, blank=True)
#     last_name = models.CharField(max_length=200, verbose_name='last name')
#     status = models.BooleanField(default=True)
#     student_type =models.CharField(max_length=100, choices=student_types, default='member')
    
#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"
    




# class Student_Profile(models.Model):
#     student = models.OneToOneField(Student,on_delete=models.CASCADE)
#     bio = models.TextField()
#     date_of_birth =models.DateField()
#     address = models.CharField(max_length=300)
#     rating = models.FloatField(default=0.0)
#     # 
#     date_join = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return f"{self.student.username}"
    
    
    



# class Program(models.Model):
#     courses = models.CharField(max_length=500)
#     grade = models.IntegerField(default=0.0)
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     def __str__(self):
#         return f"{self.courses}"

    

   
    



# class CohortGroup(models.Model):
#     name = models.CharField(max_length=200)
#     date_join = models.DateTimeField(auto_now_add=True)
#     students = models.ManyToManyField(Student)
#     def __str__(self):
#         return f"{self.name}"



# from django.db import models

# class User(models.Model):
#     STATUS_CHOICES = [
#         ('online', 'Online Exam'),
#         ('class', 'Class Exam'),
#         ('missed', 'Missed Exam'),
#     ]
    
#     profile_image = models.URLField(max_length=200, verbose_name="Profile Image URL")
#     full_name = models.CharField(max_length=100)
#     cohort = models.CharField(max_length=50)
#     program = models.CharField(max_length=100)
#     status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='online')
#     date_joined = models.DateField()
#     rating = models.DecimalField(max_digits=2, decimal_places=1)

#     def __str__(self):
#         return self.full_name


from django.db import models
from django import forms



class Student(models.Model):
    # Fields for the Student model

    profile_image = models.URLField(max_length=200, verbose_name="Profile Image URL")
    full_name = models.CharField(max_length=100)
    cohort = models.CharField(max_length=50)
    program = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    date_joined = models.DateField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)

class Program(models.Model):
    name = models.CharField(max_length=100, default='Default Program')   # Add appropriate fields
    # Add any other fields necessary for your program

    def __str__(self):
        return self.name

class Student_Profile(models.Model):
    # Fields for the Student_Profile model
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    date_join = models.DateField()
    address = models.CharField(max_length=255)

class CohortGroup(models.Model):
    # Fields for the CohortGroup model
    name = models.CharField(max_length=100)
    date_join = models.DateField()

 # Add a default value
    # Add any other fields necessary for your program

    def __str__(self):
        return self.name


    def __str__(self):
        return self.name


