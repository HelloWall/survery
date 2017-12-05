from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

from app01 import models
def login(request):
    if request.method=="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = models.Userinfo.objects.filter(username=username,password=password).first()
        request.session["username"]=user.username
        return redirect("/home/")

    return render(request,"login.html")



def home(request):
    username = request.session.get("username")
    class_list = models.Lesson.objects.all()
    return render(request,"home.html",{"class_list":class_list})