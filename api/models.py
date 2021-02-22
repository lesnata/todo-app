from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# DEFAULT_USER = User.objects.get(username="default-user")
# DEFAULT_USER_ID = DEFAULT_USER.id


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.title
