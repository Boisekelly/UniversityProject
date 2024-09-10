from django.urls import path
from .views import (
    UniversityListView, UniversityDetailView, UniversityCreateView, UniversityUpdateView,
    DepartmentListView, DepartmentDetailView, DepartmentCreateView, DepartmentUpdateView,
    HeadinstructorListView, HeadinstructorDetailView, HeadinstructorCreateView, HeadinstructorUpdateView,
    InstructorListView, InstructorDetailView, InstructorCreateView, InstructorUpdateView,
    ClassroomListView, ClassroomDetailView, ClassroomCreateView, ClassroomUpdateView,
    CourseListView, CourseDetailView, CourseCreateView, CourseUpdateView,
    StudentListView, StudentDetailView, StudentCreateView, StudentUpdateView,
    ScheduleListView, ScheduleDetailView, ScheduleCreateView, ScheduleUpdateView,
    EnrollmentListView, EnrollmentDetailView, EnrollmentCreateView, EnrollmentUpdateView
)

urlpatterns = [
    path('universities/', UniversityListView.as_view(), name='university_list'),
    path('universities/<int:pk>/', UniversityDetailView.as_view(), name='university_detail'),
    path('universities/create/', UniversityCreateView.as_view(), name='university_create'),
    path('universities/<int:pk>/edit/', UniversityUpdateView.as_view(), name='university_update'),

    path('departments/', DepartmentListView.as_view(), name='department_list'),
    path('departments/<int:pk>/', DepartmentDetailView.as_view(), name='department_detail'),
    path('departments/create/', DepartmentCreateView.as_view(), name='department_create'),
    path('departments/<int:pk>/edit/', DepartmentUpdateView.as_view(), name='department_update'),

    path('headinstructors/', HeadinstructorListView.as_view(), name='instructor_list'),
    path('headinstructors/<int:pk>/', HeadinstructorDetailView.as_view(), name='instructor_detail'),
    path('headinstructors/create/', HeadinstructorCreateView.as_view(), name='instructor_create'),
    path('headinstructors/<int:pk>/edit/', HeadinstructorUpdateView.as_view(), name='instructor_update'),

    path('instructors/', InstructorListView.as_view(), name='instructor_list'),
    path('instructors/<int:pk>/', InstructorDetailView.as_view(), name='instructor_detail'),
    path('instructors/create/', InstructorCreateView.as_view(), name='instructor_create'),
    path('instructors/<int:pk>/edit/', InstructorUpdateView.as_view(), name='instructor_update'),

    path('classrooms/', ClassroomListView.as_view(), name='classroom_list'),
    path('classrooms/<int:pk>/', ClassroomDetailView.as_view(), name='classroom_detail'),
    path('classrooms/create/', ClassroomCreateView.as_view(), name='classroom_create'),
    path('classrooms/<int:pk>/edit/', ClassroomUpdateView.as_view(), name='classroom_update'),

    path('courses/', CourseListView.as_view(), name='course_list'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('courses/create/', CourseCreateView.as_view(), name='course_create'),
    path('courses/<int:pk>/edit/', CourseUpdateView.as_view(), name='course_update'),

    path('students/', StudentListView.as_view(), name='student_list'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
    path('students/create/', StudentCreateView.as_view(), name='student_create'),
    path('students/<int:pk>/edit/', StudentUpdateView.as_view(), name='student_update'),

    path('schedules/', ScheduleListView.as_view(), name='schedule_list'),
    path('schedules/<int:pk>/', ScheduleDetailView.as_view(), name='schedule_detail'),
    path('schedules/create/', ScheduleCreateView.as_view(), name='schedule_create'),
    path('schedules/<int:pk>/edit/', ScheduleUpdateView.as_view(), name='schedule_update'),

    path('enrollments/', EnrollmentListView.as_view(), name='enrollment_list'),
    path('enrollments/<int:pk>/', EnrollmentDetailView.as_view(), name='enrollment_detail'),
    path('enrollments/create/', EnrollmentCreateView.as_view(), name='enrollment_create'),
    path('enrollments/<int:pk>/edit/', EnrollmentUpdateView.as_view(), name='enrollment_update'),
]





