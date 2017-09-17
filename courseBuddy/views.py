from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'courseBuddy/index.html')

def details(request):
    return render(request, 'courseBuddy/details.html')