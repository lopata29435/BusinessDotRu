from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models, serializers
from django.shortcuts import render
import logging

class UserProfileAPIView(APIView):
    serializer_class = serializers.UserProfileSerializer

    def get(self, request):
        return render(request, "index.html")

    def post(self, request):
        serializer = self.serializer_class(data=request.data, files=request.FILES)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

