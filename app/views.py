from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import University, Department, Headinstructor, Instructor, Classroom, Course, Student, Schedule, Enrollment

# List Views
class UniversityListView(ListView):
    model = University
    template_name = 'university_list.html'
    context_object_name = 'universities'

class DepartmentListView(ListView):
    model = Department
    template_name = 'department_list.html'
    context_object_name = 'departments'

class HeadinstructorListView(ListView):
    model = Headinstructor
    template_name = 'headinstructor_list.html'
    context_object_name = 'headinstructors'

class InstructorListView(ListView):
    model = Instructor
    template_name = 'instructor_list.html'
    context_object_name = 'instructors'

class ClassroomListView(ListView):
    model = Classroom
    template_name = 'classroom_list.html'
    context_object_name = 'classrooms'

class CourseListView(ListView):
    model = Course
    template_name = 'course_list.html'
    context_object_name = 'courses'

class StudentListView(ListView):
    model = Student
    template_name = 'student_list.html'
    context_object_name = 'students'

class ScheduleListView(ListView):
    model = Schedule
    template_name = 'schedule_list.html'
    context_object_name = 'schedules'

class EnrollmentListView(ListView):
    model = Enrollment
    template_name = 'enrollment_list.html'
    context_object_name = 'enrollments'

# Detail Views
class UniversityDetailView(DetailView):
    model = University
    template_name = 'university_detail.html'
    context_object_name = 'univname'

class DepartmentDetailView(DetailView):
    model = Department
    template_name = 'department_detail.html'
    context_object_name = 'department'

class HeadinstructorDetailView(DetailView):
    model = Headinstructor
    template_name = 'headinstructor_detail.html'
    context_object_name = 'headinstructors'

class InstructorDetailView(DetailView):
    model = Instructor
    template_name = 'instructor_detail.html'
    context_object_name = 'instructor'

class ClassroomDetailView(DetailView):
    model = Classroom
    template_name = 'classroom_detail.html'
    context_object_name = 'classroom'

class CourseDetailView(DetailView):
    model = Course
    template_name = 'course_detail.html'
    context_object_name = 'course'

class StudentDetailView(DetailView):
    model = Student
    template_name = 'student_detail.html'
    context_object_name = 'student'

class ScheduleDetailView(DetailView):
    model = Schedule
    template_name = 'schedule_detail.html'
    context_object_name = 'schedule'

class EnrollmentDetailView(DetailView):
    model = Enrollment
    template_name = 'enrollment_detail.html'
    context_object_name = 'enrollment'

# Create Views
class UniversityCreateView(CreateView):
    model = University
    template_name = 'university_form.html'
    fields = ['univname']

class DepartmentCreateView(CreateView):
    model = Department
    template_name = 'department_form.html'
    fields = ['deptname', 'university']

class HeadinstructorCreateView(CreateView):
    model = Headinstructor
    template_name = 'headinstructor_form.html'
    fields = ['headinstructorname', 'department']

class InstructorCreateView(CreateView):
    model = Instructor
    template_name = 'instructor_form.html'
    fields = ['instructorname', 'department']

class ClassroomCreateView(CreateView):
    model = Classroom
    template_name = 'classroom_form.html'
    fields = ['classroomnumber']

class CourseCreateView(CreateView):
    model = Course
    template_name = 'course_form.html'
    fields = ['coursename', 'instructor']

class StudentCreateView(CreateView):
    model = Student
    template_name = 'student_form.html'
    fields = ['studentname', 'courses']

class ScheduleCreateView(CreateView):
    model = Schedule
    template_name = 'schedule_form.html'
    fields = ['scheduletime']

class EnrollmentCreateView(CreateView):
    model = Enrollment
    template_name = 'enrollment_form.html'
    fields = ['enrollmentdate']

#Update Views
class UniversityUpdateView(UpdateView):
    model = University
    template_name = 'university_form.html'
    fields = ['univname']

class DepartmentUpdateView(UpdateView):
    model = Department
    template_name = 'department_form.html'
    fields = ['deptname', 'university']

class HeadinstructorUpdateView(UpdateView):
    model = Headinstructor
    template_name = 'headinstructor_form.html'
    fields = ['headinstructorname', 'department']

class InstructorUpdateView(UpdateView):
    model = Instructor
    template_name = 'instructor_form.html'
    fields = ['instructorname', 'department']

class ClassroomUpdateView(UpdateView):
    model = Classroom
    template_name = 'classroom_form.html'
    fields = ['classroomnumber']

class CourseUpdateView(UpdateView):
    model = Course
    template_name = 'course_form.html'
    fields = ['coursename', 'instructor']

class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'student_form.html'
    fields = ['studentname', 'courses']

class ScheduleUpdateView(UpdateView):
    model = Schedule
    template_name = 'schedule_form.html'
    fields = ['scheduletime']

class EnrollmentUpdateView(UpdateView):
    model = Enrollment
    template_name = 'enrollment_form.html'
    fields = ['enrollmentdate']
