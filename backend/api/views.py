from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics

from .models import Project, Service, Reviews
from .serializers import ProjectSerializer, ServicesSerializer, ReviewsSerializer

#projects
class ProjectsListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'id'

# services
class ServicesListCreateView(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServicesSerializer
class ServicesRetrieveUpdateDestroyView(generics.RetrieveUpdateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServicesSerializer
    lookup_field = 'id'

#reviews
class ReviewsListCreateView(generics.ListCreateAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
class ReviewsRetrieveUpdateDestroyView(generics.RetrieveUpdateAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    lookup_field = 'id'