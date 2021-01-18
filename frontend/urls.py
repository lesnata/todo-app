from django.urls import path
from . import views
# from ./api/views.py import UserRegistration


urlpatterns = [
    path('', views.list, name='list'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.login_page, name='login_page'),
    path('logout/', views.logout_page, name="logout_page")
    # path('/auth/users/', views.UserRegistration.as_view(), name="authorization")
]