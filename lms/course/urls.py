from django.urls import path
from . import views

urlpatterns = [
    path("", views.course_list , name="course_list"),
    path("<int:id>/", views.course_details , name="course_details"),
]