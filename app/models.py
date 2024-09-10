from django.db import models
from django.db.models import Count

class University(models.Model):
    univname = models.TextField(max_length=75)
   
    def __str__(self):
        return self.univname

class Department(models.Model):
    deptname = models.CharField(max_length=75)
    university = models.ForeignKey(University, on_delete=models.CASCADE)

    def __str__(self):
        return self.deptname
    
    def totalstudents(self):
        return self.student_set.count()
    
class Headinstructor(models.Model):
    headinstructorname = models.CharField(max_length=75)
    department = models.OneToOneField(Department, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.headinstructorname
    
class Instructor(models.Model):
    instructorname = models.CharField(max_length=75)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.instructorname
      
    
class Course(models.Model):
    coursename = models.CharField(max_length=100)
    instructor = models.ForeignKey(Instructor, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.coursename
    

class Student(models.Model):
    studentname = models.CharField(max_length=75)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return f"{self.studentname} {self.courses}"
    
    def totalcourses(self):
        return self.course_set.count()

class Classroom(models.Model):
    classroomnumber = models.IntegerField()

    def __str__(self):
        return self.classroomnumber

class Schedule(models.Model):
    scheduletime = models.CharField()
    classrooms = models.ManyToManyField(Classroom)

    def __str__(self):
        return self.scheduletime

class Enrollment(models.Model):
    enrollmentdate = models.IntegerField()

    def __str__(self):
        return self.enrollmentdate










