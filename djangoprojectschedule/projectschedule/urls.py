from django.urls import path
from .views import (
    DeveloperListCreateAPIView,
    DeveloperRetrieveUpdateAPIView,
    ProjectListCreateAPIView,
    ProjectRetrieveUpdateAPIView,
    TeamListCreateAPIView,
    TeamRetrieveUpdateAPIView,
    WorkingOnListCreateAPIView,
    WorkingOnRetrieveUpdateAPIView,
)

urlpatterns = [
    path('developers/', DeveloperListCreateAPIView.as_view(), name='developer-list-create'),
    path('developers/<int:pk>/', DeveloperRetrieveUpdateAPIView.as_view(), name='developer-retrieve-update'),
    path('projects/', ProjectListCreateAPIView.as_view(), name='project-list-create'),
    path('projects/<int:pk>/', ProjectRetrieveUpdateAPIView.as_view(), name='project-retrieve-update'),
    path('teams/', TeamListCreateAPIView.as_view(), name='team-list-create'),
    path('teams/<int:pk>/', TeamRetrieveUpdateAPIView.as_view(), name='team-retrieve-update'),
    path('working-on/', WorkingOnListCreateAPIView.as_view(), name='workingon-list-create'),
    path('working-on/<int:pk>/', WorkingOnRetrieveUpdateAPIView.as_view(), name='workingon-retrieve-update'),
]
