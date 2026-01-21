from django.urls import path
from .views import apply_job, view_applications

urlpatterns = [
    path('apply/<int:job_id>/', apply_job, name='apply_job'),
    path('job/<int:job_id>/', view_applications, name='view_applications'),
]
