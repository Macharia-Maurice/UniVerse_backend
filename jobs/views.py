from django.shortcuts import render
from . import models
from . import serializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny,IsAuthenticatedOrReadOnly
from posts.permissions import IsOwnerOrReadOnly
from accounts.models import UserProfile
from django.db.models import Q
from .serializers import JobSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.utils.translation import gettext_lazy as _
from .models import Job

class ListCreateJob(generics.ListCreateAPIView):
    queryset=models.Job.objects.all()
    serializer_class=serializers.JobSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        user_profile = self.request.user.user_profile
        serializer.save(author=user_profile)
   
class JobDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Job.objects.all()
    serializer_class = serializers.JobSerializer 
    permission_classes = [IsOwnerOrReadOnly]


class JobSearchView(generics.GenericAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = JobSerializer

    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('q', '')

        if not query:
            return Response({'error': _('Query parameter "q" is required.')}, status=status.HTTP_400_BAD_REQUEST)

        job_results = Job.objects.filter(
            Q(job_owner__user__first_name__icontains=query) |
            Q(title__icontains=query) | 
            Q(description__icontains=query) |
            Q(application_deadline__icontains=query)
        )

        job_serializer = self.get_serializer(job_results, many=True)

        return Response({'jobs': job_serializer.data})

    
    