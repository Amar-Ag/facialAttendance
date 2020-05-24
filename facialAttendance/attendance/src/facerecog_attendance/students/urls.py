from django.urls import path
from .views import add_student,edit_student,profile, camera
from pages.views import all_student

urlpatterns = [
    path('add/', add_student, name="addStudent"),
    path('all/', all_student, name="allStudent"),
    path('edit/<int:id>', edit_student, name="editStudent"),
    path('camera/', camera, name="camera"),
    path('profile/',profile, name="profile"),
]