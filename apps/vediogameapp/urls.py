from django.urls import path
from . import views

urlpatterns = [
    path("", views.landingpage , name = "landing-page"),
    path("list", views.list , name = "list-page")
]
