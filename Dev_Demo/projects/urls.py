from django.urls import path

# from projects.views import get_project, create_project, put_project, delete_project
# from projects import views
from . import views

urlpatterns = [
    # path('get/', views.get_project),
    # path('create/', views.create_project),
    # path('put/', views.put_project),
    # path('delete/', views.delete_project),

    # path('projects/', views.projects),
    path('<int:pk>/', views.ProjectsView.as_view()),
]
