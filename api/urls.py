from django.urls import path
from . import views
# from rest_framework.auth import views


urlpatterns = [
    path('tasks/', views.task_collection, name="task-collection"),
    path('tasks/<str:pk>', views.task_element, name="task-element"),
    path('account/register', views.registration, name="registration"),
]
