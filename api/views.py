from django.http import HttpResponse
from .serializers import TaskSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Task


# RESTful Structure for User:
# /tasks/:              [COLLECTION]
#     -> GET all tasks
#     -> POST new task
#
# /tasks/<pk>:          [ELEMENT]
#     -> GET task[id]
#     -> POST task[id] update
#     -> DELETE task[id]


@api_view(['GET', 'POST'])
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


@api_view(['GET', 'POST', 'DELETE'])
def task_element(request, pk):
    try:
        user = request.user
        task = Task.objects.filter(user=user.id).get(pk=pk)
    except Task.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    elif request.method == "POST":
        data = {'user': user.id, 'title': request.data.get('title')}
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    elif request.method == "DELETE":
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)












# #from django.shortcuts import render
# #from django.http import JsonResponse
# #from rest_framework import permissions
# from rest_framework.decorators import api_view
# #from rest_framework.generics import CreateAPIView
# from rest_framework.response import Response
# #from rest_framework.decorators import permission_classes, authentication_classes
# #from rest_framework.permissions import IsAuthenticated
# #from rest_framework.authentication import JSONWebTokenAuthentication
# from .serializers import TaskSerializer
# from django.contrib.auth.models import User
# from .models import Task
# # Create your views here.
#
# #
# # class UserRegistration(CreateAPIView):
# #     model = User
# #     permission_classes = [
# #         permissions.AllowAny
# #     ]
# #     serializer_class = UserRegistrationSerializer
# #
#
#
# @api_view(['GET'])
# def apiOverview(request):
#     api_urls = {
#         'List':'/task-list/',
#         'Detail View':'/task-detail/<str:pk>',
#         'Create':'/task-create/',
#         'Update':'/task-update/<str:pk>/',
#         'Delete':'/task-delete/<str:pk>',
#     }
#     return Response(api_urls)
#
#
# @api_view(['GET'])
# def taskList(request):
#     user = request.user
#     tasks = Task.objects.filter(id=user.id)
#     serializer = TaskSerializer(tasks, many=True)
#     # tasks = Task.objects.all().order_by('-id')
#     # serializer = TaskSerializer(tasks, many=True)
#     return Response(serializer.data)
#
#
# @api_view(['GET'])
# def taskDetail(request, pk):
#     task = Task.objects.get(id=pk)
#     serializer = TaskSerializer(task, many=False)
#     return Response(serializer.data)
#
#
# @api_view(['POST'])
# def taskCreate(request):
#     # user = request.user
#     serializer = TaskSerializer(data=request.data)
#
#     if serializer.is_valid():
#         serializer.save()
#
#     return Response(serializer.data)
#
#
# @api_view(['POST'])
# def taskUpdate(request, pk):
#     task = Task.objects.get(id=pk)
#     serializer = TaskSerializer(instance=task, data=request.data)
#
#     if serializer.is_valid():
#         serializer.save()
#
#     return Response(serializer.data)
#
#
#
# @api_view(['DELETE'])
# #@permission_classes((IsAuthenticated, ))
# #@authentication_classes([JSONWebTokenAuthentication, ])
# def taskDelete(request, pk):
#     task = Task.objects.get(id=pk)
#     task.delete()
#     return Response('Task successfully deleted!')
