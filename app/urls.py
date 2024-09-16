from django.urls import path
from . import views
from .views import (
    UniversityListView, UniversityDeleteView, UniversityUpdateView,
    DepartmentListView, DepartmentDeleteView, DepartmentUpdateView,
    HeadinstructorListView, HeadinstructorDeleteView, HeadinstructorUpdateView,
    InstructorListView, InstructorDeleteView, InstructorUpdateView,
    ClassroomListView, ClassroomDeleteView, ClassroomUpdateView,
    CourseListView, CourseDeleteView, CourseUpdateView,
    StudentListView, StudentDeleteView, StudentUpdateView,
    ScheduleListView, ScheduleDeleteView, ScheduleUpdateView,
    EnrollmentListView, EnrollmentDeleteView, EnrollmentUpdateView,
)

urlpatterns = [
    #URL Paths For The University Field
    path('university_list/', UniversityListView.as_view(), name='university_list'),
    path('university_delete/<pk>', UniversityDeleteView.as_view(), name='university_delete'),
    path('university_form/<pk>', UniversityUpdateView.as_view(), name='university_form'),
    
    #URL Paths For The Department Field
    path('department_list', DepartmentListView.as_view(), name='department_list'),
    path('department_delete/<pk>', DepartmentDeleteView.as_view(), name='department_delete'),
    path('department__form/<pk>', DepartmentUpdateView.as_view(), name='department_form'),

    #URL Paths For The Headinstructor Field
    path('headinstructor_list', HeadinstructorListView.as_view(), name='headinstructor_list'),
    path('headinstructor_delete/<pk>', HeadinstructorDeleteView.as_view(), name='headinstructor_delete'),
    path('headinstructors_form/<pk>', HeadinstructorUpdateView.as_view(), name='headinstructor_form'),

    #URL Paths For Instructor Field
    path('instructor_list', InstructorListView.as_view(), name='instructor_list'),
    path('instructor_delete/<pk>', InstructorDeleteView.as_view(), name='instructor_delete'),
    path('instructor_form/<pk>', InstructorUpdateView.as_view(), name='instructor_form'),

    #URL Paths For The Classroom Field
    path('classroom_list', ClassroomListView.as_view(), name='classroom_list'),
    path('classroom_delete/<pk>', ClassroomDeleteView.as_view(), name='classroom_delete'),
    path('classroom_form/<pk>', ClassroomUpdateView.as_view(), name='classroom_form'),

    #URL Paths For The Course Field
    path('course_list', CourseListView.as_view(), name='course_list'),
    path('course_delete/<pk>', CourseDeleteView.as_view(), name='course_delete'),
    path('course_form/<pk>', CourseUpdateView.as_view(), name='course_form'),

    #URL Paths For The Student Field
    path('student_list', StudentListView.as_view(), name='student_list'),
    path('student_delete/<pk>', StudentDeleteView.as_view(), name='student_delete'),
    path('student_form/<pk>', StudentUpdateView.as_view(), name='student_form'),

    #URL Paths For The Schedule Field
    path('schedule_list', ScheduleListView.as_view(), name='schedule_list'),
    path('schedule_delete/<pk>', ScheduleDeleteView.as_view(), name='schedule_delete'),
    path('schedule_form/<pk>', ScheduleUpdateView.as_view(), name='schedule_form'),

    #URL Paths For The Enrollment Field
    path('enrollment_list', EnrollmentListView.as_view(), name='enrollment_list'),
    path('enrollment_delete/<pk>', EnrollmentDeleteView.as_view(), name='enrollment_delete'),
    path('enrollment_form/<pk>', EnrollmentUpdateView.as_view(), name='enrollment_form'),
]





