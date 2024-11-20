from django.urls import path
from . import views

app_name = 'sunshineEmr'

urlpatterns = [
    path('', views.index, name="index"),
]