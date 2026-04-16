from django.urls import path

from myapp.views import home, addResume, viewResume, editResume, deleteResume

urlpatterns = [
    path("", home, name="home"),
    path("addResume/", addResume, name="addResume"),
    path("viewResume/<str:id>/", viewResume, name="viewResume"),
    path("editResume/<str:id>/", editResume, name="editResume"),
    path("deleteResume/<str:id>/", deleteResume, name="deleteResume")
]
