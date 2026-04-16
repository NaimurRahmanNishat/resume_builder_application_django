from django.urls import path

from myapp.views import home, addResume

urlpatterns = [
    path("", home, name="home"),
    path("addResume/", addResume, name="addResume")
]
