from django.urls import path
from placticeapi import views

app_name = "placticeapi"
urlpatterns = [
    path("v1/persons/", views.person_list, name="person_list"),
]
