from django.shortcuts import render

from django.http import HttpResponseRedirect

from .forms import NameForm



def index(request):
    return render(request, 'courseBuddy/index.html')

def details(request):
    return render(request, 'courseBuddy/details.html')

def peoples_list(request):
    the_peeps_file = 'courseBuddy/people_data.txt'

    with open(the_peeps_file,'r') as f:
        the_peeps = f.readlines()
    the_peeps = [x.strip() for x in the_peeps]
    html_string = '<!DOCTYPE html>'
    html_string += '<html>'
    html_string += '<head><title>Peoples Directory</title></head>'
    html_string += '<body>'

    for p in the_peeps:
        psplits = p.split(',')
        id = psplits[0]
        first = psplits[1]
        last = psplits[2]
        year = psplits[3]
        html_string += '<h1>'+id+': '+first+' '+last+', '+year+'</h1>'

    html_string += '</body>'
    html_string += '</html>'
    with open('courseBuddy/templates/courseBuddy/peeps.html','w') as html_file:
        html_file.write(html_string)
        html_file.close()
    f.close()
    return render(request, 'courseBuddy/peeps.html')

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





