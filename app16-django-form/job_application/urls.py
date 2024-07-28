from django.urls import path
from . import views

urlpatterns = [
    # name="xxx" should be the same as views.xxx
    path("", views.index, name="index")
]
