from django.urls import path
from . import views

app_name = 'Hello_World'

urlpatterns = [
    path('', views.index, name='index'),
]