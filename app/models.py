from django.db import models
from django.db.models import Count



#This Is The University Model
class University(models.Model):
    univname = models.TextField(max_length=75)
   
    def __str__(self):
        return self.univname

#This Is The Department Model
class Department(models.Model):
    deptname = models.CharField(max_length=75)
    university = models.ForeignKey(University, on_delete=models.CASCADE)

    def __str__(self):
        return self.deptname
    
    def totalstudents(self):
        return self.student_set.count()

#This Is The Headinstructor Model
class Headinstructor(models.Model):
    headinstructorname = models.CharField(max_length=75)
    department = models.OneToOneField(Department, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.headinstructorname

#This Is The Instructor Model 
class Instructor(models.Model):
    instructorname = models.CharField(max_length=75)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.instructorname
      
#This Is The Course Model   
class Course(models.Model):
    coursename = models.CharField(max_length=100)
    instructor = models.ForeignKey(Instructor, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.coursename
    
#This Is The Student Model 
class Student(models.Model):
    studentname = models.CharField(max_length=75)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return f"{self.studentname} {self.courses}"
    
    def totalcourses(self):
        return self.course_set.count()
    
#This Is The Classroom Model 
class Classroom(models.Model):
    classroomnumber = models.IntegerField()

    def __str__(self):
        return self.classroomnumber

#This Is The Schedule Model 
class Schedule(models.Model):
    scheduletime = models.CharField()
    classrooms = models.ManyToManyField(Classroom)

    def __str__(self):
        return self.scheduletime

#This Is The Enrollment Model 
class Enrollment(models.Model):
    enrollmentdate = models.IntegerField()

    def __str__(self):
        return self.enrollmentdate










