from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def addResume(request):
    return render(request, 'addResume.html')

