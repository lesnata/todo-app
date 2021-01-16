from django.urls import path
from . import views
# from ./api/views.py import UserRegistration


urlpatterns = [
    path('', views.list, name='list'),
    path('registration/', views.registration, name='registration'),
    # path('/auth/users/', views.UserRegistration.as_view(), name="authorization")
]