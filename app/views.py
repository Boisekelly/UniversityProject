from django.shortcuts import render
from django.views.generic import ListView, DeleteView, UpdateView
from .models import University, Department, Headinstructor, Instructor, Classroom, Course, Student, Schedule, Enrollment

def name(request):
    context = {"name": "Kelly"} 
    return render(request, "base.html", context)

# List Views
class UniversityListView(ListView):
    model = University
    template_name = 'app/university_list.html'
    context_object_name = 'universities'

class DepartmentListView(ListView):
    model = Department
    template_name = 'app/department_list.html'
    context_object_name = 'departments'

class HeadinstructorListView(ListView):
    model = Headinstructor
    template_name = 'app/headinstructor_list.html'
    context_object_name = 'headinstructors'

class InstructorListView(ListView):
    model = Instructor
    template_name = 'app/instructor_list.html'
    context_object_name = 'instructors'

class ClassroomListView(ListView):
    model = Classroom
    template_name = 'app/classroom_list.html'
    context_object_name = 'classrooms'

class CourseListView(ListView):
    model = Course
    template_name = 'app/course_list.html'
    context_object_name = 'courses'

class StudentListView(ListView):
    model = Student
    template_name = 'app/student_list.html'
    context_object_name = 'students'

class ScheduleListView(ListView):
    model = Schedule
    template_name = 'app/schedule_list.html'
    context_object_name = 'schedules'

class EnrollmentListView(ListView):
    model = Enrollment
    template_name = 'app/enrollment_list.html'
    context_object_name = 'enrollments'

# Delete Views
class UniversityDeleteView(DeleteView):
    model = University
    template_name = 'app/university_delete.html'
    context_object_name = 'univname'

class DepartmentDeleteView(DeleteView):
    model = Department
    template_name = 'app/department_delete.html'
    context_object_name = 'department'

class HeadinstructorDeleteView(DeleteView):
    model = Headinstructor
    template_name = 'app/headinstructor_delete.html'
    context_object_name = 'headinstructors'

class InstructorDeleteView(DeleteView):
    model = Instructor
    template_name = 'app/instructor_delete.html'
    context_object_name = 'instructor'

class ClassroomDeleteView(DeleteView):
    model = Classroom
    template_name = 'app/classroom_delete.html'
    context_object_name = 'classroom'

class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'app/course_delete.html'
    context_object_name = 'course'

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'app/student_delete.html'
    context_object_name = 'student'

class ScheduleDeleteView(DeleteView):
    model = Schedule
    template_name = 'app/schedule_delete.html'
    context_object_name = 'schedule'

class EnrollmentDeleteView(DeleteView):
    model = Enrollment
    template_name = 'app/enrollment_delete.html'
    context_object_name = 'enrollment'


#Update Views
class UniversityUpdateView(UpdateView):
    model = University
    template_name = 'app/university_form.html'
    fields = ['univname']

class DepartmentUpdateView(UpdateView):
    model = Department
    template_name = 'app/department_form.html'
    fields = ['deptname', 'university']

class HeadinstructorUpdateView(UpdateView):
    model = Headinstructor
    template_name = 'app/headinstructor_form.html'
    fields = ['headinstructorname', 'department']

class InstructorUpdateView(UpdateView):
    model = Instructor
    template_name = 'app/instructor_form.html'
    fields = ['instructorname', 'department']

class ClassroomUpdateView(UpdateView):
    model = Classroom
    template_name = 'app/classroom_form.html'
    fields = ['classroomnumber']

class CourseUpdateView(UpdateView):
    model = Course
    template_name = 'app/course_form.html'
    fields = ['coursename', 'instructor']

class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'app/student_form.html'
    fields = ['studentname', 'courses']

class ScheduleUpdateView(UpdateView):
    model = Schedule
    template_name = 'app/schedule_form.html'
    fields = ['scheduletime']

class EnrollmentUpdateView(UpdateView):
    model = Enrollment
    template_name = 'app/enrollment_form.html'
    fields = ['enrollmentdate']
