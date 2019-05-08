from django.urls import path
from . import views

app_name = 'saml2_lib'

urlpatterns = [
    path('acs/<str:company>/<str:app>/', views.acs, name="acs"),
    path('welcome/', views.welcome, name="welcome"),
    path('denied/', views.denied, name="denied"),
]
