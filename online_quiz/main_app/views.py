from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def homepage_teacher(request):
    return render(request,'teacher/homepage.html')
def create_quiz(request):
    return render(request,'teacher/create_quiz.html')
