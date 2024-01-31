from django.shortcuts import render , redirect
from django.http import HttpResponse , HttpResponseRedirect
from .forms import RegisterForm
import numpy as np
import cv2
import time
# Create your views here.
def begin(response) :
    return render(response, "registration/main.html", {})
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/login")
    else:
        form = RegisterForm()
    return render(response,"register/register.html",{"form":form})

def main(response):
    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
    faces=[]
    while True:
        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)
            roi_gray = gray[y:y + w, x:x + w]
            roi_color = frame[y:y + h, x:x + w]


        cv2.imshow('frame', frame)

        if cv2.waitKey(1) == ord('q') or len(faces)>0 :
            
            break

    cap.release()
    cv2.destroyAllWindows()
    return  HttpResponseRedirect("/login")