from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    return render(request, 'courseBuddy/index.html')

def details(request):
    return render(request, 'courseBuddy/details.html')

@login_required
def home(request):
	return render(request, 'courseBuddy/home.html')