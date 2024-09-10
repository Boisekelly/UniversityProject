from django.contrib import admin
from .models import University, Department, Instructor, Classroom, Course, Student, Schedule, Enrollment, Headinstructor

admin.site.register(University)
admin.site.register(Department)
admin.site.register(Instructor)
admin.site.register(Classroom)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Schedule)
admin.site.register(Enrollment)
admin.site.register(Headinstructor)

class UniversityAdmin(admin.ModelAdmin):
    list_display = ('univname')
    search_fields = ('univname')
    list_filter = ('univname')

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('deptname', 'university')
    search_fields = ('deptname', 'university')
    list_filter = ('deptname', 'university')

class Headinstructor(admin.ModelAdmin):
    list_display = ('headinstructorname', 'department')
    search_fields = ('headinstructorname', 'department')
    list_filter = ('headinstructorname', 'department')

class InstructorAdmin(admin.ModelAdmin):
    list_display = ('instructorname', 'department')
    search_fields = ('instructorname', 'department')
    list_filter = ('instructorname', 'department')

class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('classroomnumber')
    search_fields = ('classroomnumber')
    list_filter = ('classroomnumber')

class CourseAdmin(admin.ModelAdmin):
    list_display = ('coursename', 'instructor')
    search_fields = ('coursename', 'instructor')
    list_filter = ('coursename', 'instructor')

class StudentAdmin(admin.ModelAdmin):
    list_display = ('studentname', 'courses')
    search_fields = ('studentname', 'courses')
    list_filter = ('studentname', 'courses')

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('scheduletime', 'classrooms')
    search_fields = ('scheduletime', 'classrooms')
    list_filter = ('scheduletime', 'classrooms')

class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('enrollmentdate')
    search_fields = ('enrollmentdate')
    list_filter = ('enrollmentdate')
