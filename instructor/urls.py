from django.urls import path, re_path
from . import views

urlpatterns = [
    path('instructor_index/', views.instructor_index, name='instructor_index'),
    path('<int:course_id>/instructor_detail/', views.instructor_detail, name='instructor_detail'),
    path('<int:course_id>/add_assignment/', views.add_assignment, name='add_assignment'),
    path('<int:course_id>/add_resource/', views.add_resource, name='add_resource'),
    path('<int:course_id>/add_notification/', views.add_notification, name='add_notification'),
    path('<int:course_id>/view_all_assignments/', views.view_all_assignments, name='view_all_assignments'),
    path('<int:assignment_id>/view_all_submissions/', views.view_all_submissions, name='view_all_submissions'),
    path('<int:assignment_id>/view_feedback/', views.view_feedback, name='view_feedback'),
]
