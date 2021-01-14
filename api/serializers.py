from rest_framework import serializers
from .models import Task, UserProfile


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class UserProfileSerialiser(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = UserProfile
        fields = '__all__'
