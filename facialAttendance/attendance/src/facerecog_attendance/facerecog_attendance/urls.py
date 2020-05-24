"""facerecog_attendance URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pages.views import admin_login_view
from administrator.views import admin_login,calendar
from pages.views import add_student_view, landingpage_view, camera
from students.views import delete_student

urlpatterns = [
    path('admin/', admin_login_view, name="admin"),
    path('dashboard/', admin_login, name="dashboard"),
    path('dashboard/add_student_view', add_student_view, name="add_student_view"),
    path('calendar/', calendar,name="calendar"),
    path('student/', include('students.urls')),
    path('student/all/delete/<int:id>', delete_student, name="deleteStudent"),
    path('', landingpage_view, name="landingpage"),
    path('camera', camera, name="recognizeface")

]
