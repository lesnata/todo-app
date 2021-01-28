from django.http import HttpResponse
from .serializers import TaskSerializer, RegistrationSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


""" 
RESTful Structure for User:
/tasks/:              [COLLECTION]
    -> GET all tasks
    -> POST new task

/tasks/<pk>:          [ELEMENT]
    -> GET task[id]
    -> PUT task[id] update
    -> DELETE task[id] 
    
"""


@api_view(['POST'])
def registration(request):
    serializer = RegistrationSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        serializer.save()
        # user = serializer.save()
        user = User.objects.get(username=serializer.data["username"])
        print('serializer')
        print(serializer)

        username = serializer.data["username"]
        email = serializer.data["email"]
        token = Token.objects.get(user=user).key

        data["username"] = username
        data["email"] = email
        data["token"] = token
        return Response(data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def task_collection(request):
    try:
        user = request.user
    except user in None:
        return HttpResponse(status=404)

    if request.method == "GET":
        user = request.user
        tasks = Task.objects.filter(user=user.id)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        data = {'user': request.user.id,
                'title': request.data.get('title')}
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def task_element(request, pk):
    try:
        user = request.user
        task = Task.objects.filter(user=user.id).get(pk=pk)
    except Task.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    elif request.method == "DELETE":
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

