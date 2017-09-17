from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import NameForm


def index(request):
    return render(request, 'courseBuddy/index.html')

def details(request):
    return render(request, 'courseBuddy/details.html')

def form(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'courseBuddy/form.html', {'form': form})

def data(request):
    newrow = ""
    newrow += request.POST["identifier"] + ", "
    newrow += request.POST["first_name"] + ", "
    newrow += request.POST["last_name"] + ", "
    newrow += request.POST["year_school"] + ", ["
    newrow += request.POST["classes"].replace(',', '%') + "]\n"
    print (newrow)
    with open("courseBuddy/people_data.txt", "a+") as myfile:
        myfile.write(newrow)
        print ("done")
    return render(request, 'courseBuddy/index.html')






