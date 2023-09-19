from django.urls import path
from . import views


urlpatterns = [
    path('', views.core_home, name='core_home'),
]