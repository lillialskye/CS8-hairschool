from django.shortcuts import render
from rest_framework import viewsets

from .models import CScheduling
from .serializers import CSchedulingSerializer

class Client_SchedulingView(viewsets.ModelViewSet):
    queryset = CScheduling.objects.all()
    serializer_class = CSchedulingSerializer
