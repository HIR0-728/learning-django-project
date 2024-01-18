from django.urls import path
from placticeapp import views

app_name = "placticeapp"
urlpatterns = [
    path("person/", views.person_list, name="person_list"),
    path("person/create/", views.person_edit, name="person_create"),
    path("person/edit/<int:person_id>/", views.person_edit, name="person_edit"),
    path("person/delete/<int:person_id>/", views.person_delete, name="person_delete"),
]
