from django.shortcuts import render, redirect
from .models import Student
import cv2
import os
import shutil
Id = 0
FName = ""
# Create your views here.
def add_student(request, *args, **kwargs):
    global Id, FName
    RollNo = request.POST.get('RollNo')
    Name = request.POST.get('FirstName')
    Id = RollNo
    FName = Name
    print(Id)
    Student.objects.create(FirstName=request.POST.get('FirstName'), LastName=request.POST.get('LastName') ,RollNo =request.POST.get('RollNo'),Email=request.POST.get('Email'),RegistrationDate=request.POST.get('RegisterDate'),
                           Class=request.POST.get('Class'),Gender=request.POST.get('Gender'),MobileNo=request.POST.get('MobileNumber'),ParentsName=request.POST.get('ParentName'),ParentMobileNo=request.POST.get('ParentNumber'),
                           BirthDate=request.POST.get('DOB'), BloodGroup=request.POST.get('BloodGroup'),Address=request.POST.get('Address'))
    os.chdir('/home/amar/BCP/FaceDb')
    try:
        os.mkdir(Id)
    except FileExistsError:
        os.rename(Id, Id)

    return redirect('add_student_view')

def edit_student(request, id, *args, **kwargs):
    student = Student.objects.get(RollNo=id)
    if request.method == 'POST':
        FirstName = request.POST.get('FirstName')
        LastName = request.POST.get('LastName')
        RollNo = request.POST.get('RollNo')
        Email = request.POST.get('Email')
        RegistrationDate = request.POST.get('RegisterDate')
        Class = request.POST.get('Class')
        Gender = request.POST.get('Gender')
        MobileNo = request.POST.get('MobileNumber')
        ParentsName = request.POST.get('ParentName')
        ParentMobileNo = request.POST.get('ParentNumber')
        BirthDate = request.POST.get('DOB')
        BloodGroup = request.POST.get('BloodGroup')
        Address = request.POST.get('Address')

        student.FirstName = FirstName
        student.LastName = LastName
        student.Email = Email
        student.RegistrationDate = RegistrationDate
        student.Class = Class
        student.Gender = Gender
        student.MobileNo = MobileNo
        student.ParentsName = ParentsName
        student.ParentMobileNo = ParentMobileNo
        student.BirthDate = BirthDate
        student.BloodGroup = BloodGroup
        student.Address = Address
        student.save()

        return redirect('allStudent')

    else:
        context = {
            'student': student
        }
        return render(request, 'edit_student.html', context)


def delete_student(request, id, *args, **kwargs):
    student = Student.objects.get(RollNo=id)
    os.chdir('/home/amar/BCP/FaceDb')
    if os.path.exists(str(student.Id)) and not os.listdir(str(student.Id)):
        os.rmdir(str(student.Id))
    else:
        shutil.rmtree(str(student.Id))
    student.delete()
    return redirect('allStudent')

def camera(request, *args, **kwargs):
    global Id
    global FName
    print("Id {}".format(Id))
    print("Name {}".format(FName))

    face_recog = cv2.CascadeClassifier('/home/amar/BCP/attendance/lib/python3.6/site-packages/cv2/data/haarcascade_frontalface_default.xml')
    print(face_recog)
    cap = cv2.VideoCapture(0)
    count = 0
    while (True):
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_recog.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            count += 1
            # print(x, y, w, h)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]
            # cv2.imwrite("/home/aashir/Documents/7th Sem/bcp/{}/user" + str(count) + ".jpg", roi_color)
            print("TYPE OF ID: {}".format(type(Id)))
            cv2.imwrite("/home/amar/BCP/FaceDb/{}/{}".format(int(Id), FName) + str(count) + ".jpg", roi_color)
            cv2.putText(frame, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow('Face', frame)

        if cv2.waitKey(100) == 13 or count == 100:
            break

    cap.release()
    cv2.destroyAllWindows()

    return redirect('add_student_view')


def profile(request):
    return render(request, 'user_profile.html')
