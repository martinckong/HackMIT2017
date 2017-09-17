from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect

from .forms import NameForm


class Person:
    def __init__(self, id, first_name, last_name, year, current_classes):
        self.ID = id
        self.first = first_name
        self.last = last_name
        self.class_year = year
        self.current_classes_list = current_classes
    def id(self):
        return self.ID
    def firstname(self):
        return self.first
    def lastname(self):
        return  self.last
    def year(self):
        return self.class_year
    def classes(self):
        copy_classes = []
        for c in self.current_classes_list:
            copy_classes.append(c)
        return  copy_classes

    def print_string(self):
        s = 'Student '+ self.first +' ' + self.last +', year '+self.class_year+' with ID '+self.ID
        s += ' is taking the following classes: '
        for c in self.current_classes_list:
            s += c +', '
        s = s.strip().rstrip(',')+'.'
        return s

def index(request):
    return render(request, 'courseBuddy/index.html')

def details(request):
    return render(request, 'courseBuddy/details.html')

@login_required
def home(request):
	return render(request, 'courseBuddy/home.html')

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
        html_string += '<p><a href =\'match/{{ \''+id+'\' }}\'> '+first+' '+last+', '+year+'</a></p>'\

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

def match(request, student_id):
    html_string ='<!DOCTYPE html><html><head><title>courseBuddy Match</title></head>'
    html_string += '<body>'
    classes_data = {}  # class number mapped to students taking class
    peoples_data = {}  # list of all peeps we have data for, also based on people's ids
    classes_listing_file = 'courseBuddy/classes_listing.txt'
    with open(classes_listing_file) as f:
        classes_content = f.read().split(',')
    classes_content = [x.strip() for x in classes_content]
    for c in classes_content:
        if len(c) > 0:
            classes_data[c.upper()] = []
            # print (classes_data)

    file_location = 'courseBuddy/people_data.txt'
    with open(file_location) as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    for c in content:
        splits = c.split(',')
        classes = splits[len(splits) - 1].strip().lstrip('[').strip(']').split('%')  # classes after last comma
        person_id = splits[0]
        # splits[0] is id, splits[1] first name, splits[2] last name, splits[3] year
        person = Person(person_id, splits[1], splits[2], splits[3], classes)
        peoples_data[person_id] = person
        for ca in classes:
            if ca in classes_data.keys():
                x = classes_data[ca]
                x.insert(0, person)
                classes_data[ca] = x
            else:
                classes_data[ca] = [person]

    current_peep = peoples_data[student_id]
    peep_name = current_peep.firstname() +' '+current_peep.lastname()
    peep_year = current_peep.year()
    html_string += '<h1><p>courseBuddy match for '+peep_name+', '+ peep_year+'.</p></h1>'
    for x_class in current_peep.classes():
        class_peeps = []
        for student in classes_data[x_class]:
            if student != current_peep:
                class_peeps.append(student)
        html_string += '<p><b>Class:' + x_class + '</b></p>'
        if len(class_peeps) != 0:
            for p in class_peeps:
                html_string += '<p> - ' + p.firstname() + ' ' + p.lastname() + ', ' + p.year() + '</p>'
        else:
            html_string += '<p>...No buddies found for class. :( </p>'

    html_string += '</body>'
    html_string += '</html>'
    with open('courseBuddy/templates/courseBuddy/buddy_match.html','w') as html_file:
        html_file.write(html_string)
        html_file.close()

    return render(request, 'courseBuddy/buddy_match.html')
