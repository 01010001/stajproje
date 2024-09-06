from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from . import models
from . import serializers
from rest_framework import generics
from .models import Developers, Projects, Teams, WorkingOn
from .serializers import DeveloperSerializer, ProjectSerializer, TeamSerializer, WorkingOnSerializer

# class DeveloperCreateAPIView(generics.ListCreateAPIView):
#     queryset = models.Developers.objects.all()
#     serializer_class = serializers.DeveloperSerializer

# @api_view(['GET'])
# def getData(request):
#     items = models.Developers.objects.all()
#     serializer = serializers.DeveloperSerializer(items, many=True)
#     return Response(serializer.data)

# @api_view(['POST'])
# def addData(request):
#     serializer = serializers.DeveloperSerializer(data=request.data)
#     if serializer.is_valid():
#         print("its valid, saving")
#         serializer.save()
#     else:
#         print("not valid", serializer.errors)
#     return Response(serializer.data)

# #deletion of certain developer rows on demand.
# @api_view(['DELETE'])
# def removeData(request, id):
# #     instance = models.Developers.objects.get(id=id)
# #     instance.delete()
# #     return Response()
#     pass

class DeveloperListCreateAPIView(generics.ListCreateAPIView):
    queryset = Developers.objects.all()
    serializer_class = DeveloperSerializer

class DeveloperRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Developers.objects.all()
    serializer_class = DeveloperSerializer

class ProjectListCreateAPIView(generics.ListCreateAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer

class ProjectRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer

class TeamListCreateAPIView(generics.ListCreateAPIView):
    queryset = Teams.objects.all()
    serializer_class = TeamSerializer

class TeamRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Teams.objects.all()
    serializer_class = TeamSerializer

class WorkingOnListCreateAPIView(generics.ListCreateAPIView):
    queryset = WorkingOn.objects.all()
    serializer_class = WorkingOnSerializer

class WorkingOnRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = WorkingOn.objects.all()
    serializer_class = WorkingOnSerializer
