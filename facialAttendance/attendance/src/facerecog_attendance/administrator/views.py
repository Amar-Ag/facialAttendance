from django.shortcuts import render, redirect
from .models import Admin
from attendance.models import Attendance
# Create your views here.
isLoggedIn = False


def admin_login(request):
    global isLoggedIn
    attendance = Attendance.objects.all()
    context = {
        'attendance': attendance
    }

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        if username and password:
            try:
                admin = Admin.objects.get(username=username, password=password)
                isLoggedIn = True
            except Admin.DoesNotExist:
                return redirect('admin')

            return render(request, 'index.html', context)
        else:
            return redirect('admin')

    if isLoggedIn:
        return render(request, 'index.html', context)
    else:
        return redirect('admin')

def calendar(request):
    return render(request, 'calendar.html')