from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Profile
from .serializers import UserSerializer, ProfileSerializer


class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = 'core/dashboard.html'
    # extra_context =

@api_view(['GET'])
def get_users(request):
    fields = ['is_superuser', 'is_staff', 'is_active']
    serializer = UserSerializer(User.objects.all(), many=True, exclude=fields)
    context = {
        'status': status.HTTP_200_OK,
        'data': [
            serializer.data,
        ]
    }
    print(context)
    return JsonResponse(context, safe=False, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_profiles(request):
    serializer = ProfileSerializer(Profile.objects.all(), many=True, depth=1)
    context = {
        'status': status.HTTP_200_OK,
        'data': [
            serializer.data,
        ]
    }
    return JsonResponse(context, safe=False, status=status.HTTP_200_OK)
