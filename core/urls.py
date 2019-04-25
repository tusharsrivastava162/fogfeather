from django.urls import path
from . import views

urlpatterns = [
    path('', views.Dashboard.as_view()),
    path('users/', views.get_users),
    path('profiles/', views.get_profiles),
]
