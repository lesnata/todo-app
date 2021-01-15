from rest_framework import serializers
from .models import Task
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = '__all__'



# class UserProfileSerializer(serializers.ModelSerializer):
#
#     password = serializers.CharField(write_only=True)
#
#     def create(self, validated_data):
#         user = UserProfile.objects.create(
#             username=validated_data['username']
#         )
#         user.set_password(validated_data['password'])
#         user.save()
#         return user
#
#     class Meta:
#         model = UserProfile
#         fields = '__all__'
