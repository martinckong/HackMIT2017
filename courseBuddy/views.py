from django.shortcuts import render
import os
# Create your views here.


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


