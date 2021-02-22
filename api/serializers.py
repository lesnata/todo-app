from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    #  IF REWRITING save() method
    #
    # def save(self):
    #     user = User(email=self.validated_data["email"],
    #                 username=self.validated_data["username"],
    #                 password=self.validated_data["password"],
    #                 )
    #     # password = self.validated_data["password"],
    #     # password2 = self.validated_data["password2"],
    #     # if password != password2:
    #     #     raise serializers.ValidationError({"password":
    #     "Passwords do not match"})
    #
    #     # user.set_password(password)
    #     user.save()
    #     return user
