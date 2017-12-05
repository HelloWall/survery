import json
from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

from app01 import models
def login(request):
    if request.method=="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = models.Userinfo.objects.filter(username=username,password=password).first()
        if user:
            print(user.username)
            request.session["username"]=user.username
            return redirect("/home/")
    return render(request,"login.html")



def home(request):
    username = request.session.get("username")
    questionnaire_list = models.Questionnaire.objects.all()
    return render(request,"home.html",{"questionnaire_list":questionnaire_list})



def student(request):
    student_list = models.Student.objects.all()
    return render(request,"student.html",{"student_list":student_list})

def lesson(request):
    lesson_list = models.Lesson.objects.all()
    return render(request,"lesson.html",{"lesson_list":lesson_list})


def questionnaire(request):
    questionnaire_list = models.Questionnaire.objects.all()
    return render(request, "questionnaire.html", {"questionnaire_list": questionnaire_list})


def trouble(request,questionnaire_id):

    questionnaire_list=models.Questionnaire.objects.filter(id=questionnaire_id).first()
    genre_LIst = models.Genre.objects.all()
    return render(request,"trouble.html",{"questionnaire_list":questionnaire_list,"genre_LIst":genre_LIst})



def add_question(request):
    genre_dict={"genre":[]}
    genre_list = models.Genre.objects.all()
    for genre in genre_list:
        genre_dict['genre'].append(genre.title)
    return HttpResponse(json.dumps(genre_dict))


def result(request):
    print(request)
    return render(request,"result.html")