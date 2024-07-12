from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:course_id>/detail/', views.detail, name='detail'),
    path('<int:assignment_id>/upload_submission/', views.upload_submission, name='upload_submission'),
    path('<int:course_id>/view_assignments/', views.view_assignments, name='view_assignments'),
    path('<int:course_id>/view_resources/', views.view_resources, name='view_resources'),
]
