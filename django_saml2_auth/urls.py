from django.urls import path
from . import views

app_name = 'django_saml2_auth'

urlpatterns = [
    path('acs/<str:company>/<str:app>/', views.acs, name="acs"),
    path('welcome/', views.welcome, name="welcome"),
    path('denied/', views.denied, name="denied"),
]
