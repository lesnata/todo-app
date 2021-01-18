from django.contrib.auth.models import User
from django.db import models

# Create your models here.


DEFAULT_USER = User.objects.get(username="admin-lesna")
DEFAULT_USER_ID = DEFAULT_USER.id


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.title


# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
#     date_joined = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.user.username
