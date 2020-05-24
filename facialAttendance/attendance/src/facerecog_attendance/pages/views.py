from django.shortcuts import render, redirect
from students.models import Student
import cv2
import pickle
from attendance.models import Attendance
import time

Id = 0
Name = ""

# Create your views here.
def admin_login_view(request, *args, **kwargs):
    return render(request, 'login-form.html')

def add_student_view(request, *args, **kwargs):
    return render(request, 'add_student.html')

def all_student(request):
    student = Student.objects.all()
    context = {
        'students': student
    }
    return render(request, 'all_students.html', context)

def landingpage_view(request, *args, **kwargs):

    return render(request, 'landing-page.html')

def camera(request):
    global Id, Name
    systemDate = time.strftime("%d/%m/%Y")
    face_recog = cv2.CascadeClassifier(
        '/home/amar/BCP/attendance/lib/python3.6/site-packages/cv2/data/haarcascade_frontalface_default.xml')
    print(face_recog)
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('/home/amar/BCP/attendance/src/facerecog_attendance/pages/trainer.yml')
    labels = {"person_name":1}
    with open('/home/amar/BCP/attendance/src/facerecog_attendance/pages/labels.pickle', 'rb') as f:
        og_labels = pickle.load(f)
        labels = {v: k for k, v in og_labels.items()}

    cap = cv2.VideoCapture(0)
    count = 0
    while (True):
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_recog.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            count += 1
            # print(.x, y, w, h)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]
            id_, conf = recognizer.predict(roi_gray)
            if conf >= 30 and conf <= 85:
                font = cv2.FONT_HERSHEY_SIMPLEX
                Id = id_
                Name = labels[id_]
                name = labels[id_]
                color = (120, 255, 100)
                stroke = 3
                cv2.putText(frame, name, (x,y), font, 1, color, stroke, cv2.LINE_AA)
            # cv2.imwrite("/home/aashir/Documents/7th Sem/bcp/{}/user" + str(count) + ".jpg", roi_color)
            # cv2.imwrite("/home/amar/BCP/FaceDb/{}/{}".format(int(Id), FName) + str(count) + ".jpg", roi_color)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)



        cv2.imshow('Face', frame)

        if cv2.waitKey(100) == 13 or count == 100:
            break

    if Id > 0 and Name != "":
        RollNo = Id
        attendance = Attendance.objects.all()
        if not attendance.exists():
            Attendance.objects.create(RollNo=RollNo, Name=Name, Status=1, Date=systemDate)
        else:
            attendanceStd = Attendance.objects.filter(Name=Name, Date=systemDate)
            if not attendanceStd.exists():
                Attendance.objects.create(RollNo=RollNo, Name=Name, Status=1, Date=systemDate)
            else:
                print("Attendance already taken")

    cap.release()
    cv2.destroyAllWindows()

    return redirect('landingpage')