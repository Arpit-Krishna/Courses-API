from django.urls import path
from .views import (
    CourseListCreateView, CourseDetailView,
    CourseInstanceListCreateView, CourseInstanceDetailView
)

urlpatterns = [
    path('courses/', CourseListCreateView.as_view(), name='course-list'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('instances/<int:year>/<int:semester>/', CourseInstanceListCreateView.as_view(), name='course-instance-list'),
    path('instances/<int:year>/<int:semester>/<int:pk>/', CourseInstanceDetailView.as_view(), name='course-instance-detail'),
]
