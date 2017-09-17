import os
classes_data = {} #class number mapped to students taking class
peoples_data = [] #list of all peeps we have data for
classes_listing_file = 'classes_listing.txt'
with open(classes_listing_file) as f:
    classes_content = f.read().split(',')
classes_content = [x.strip() for x in classes_content]

for c in classes_content:
    if len(c) > 0:
        classes_data[c.upper()] = []
#print (classes_data)


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
    def schoolyear(self):
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

file_location = './people_data.txt'
with open(file_location) as f:
    content = f.readlines()
content = [x.strip() for x in content]
for c in content:
    #print(c)
    splits = c.split(',')
    classes = splits[len(splits)-1].strip().lstrip('[').strip(']').split('%') #classes after last comma
    person_id = splits[0]
    #splits[0] is id, splits[1] first name, splits[2] last name, splits[3] year
    person = Person(person_id,splits[1],splits[2],splits[3],classes)
    peoples_data.append(person)
    #print (person.print_string())
    for ca in classes:
        if ca in classes_data.keys():
            x= classes_data[ca]
            x.insert(0,person)
            #print (x)
            classes_data[ca] = x
        else:
            #print('Added class '+ca+ ' to class listing')
            classes_data[ca] = [person]
    #print (classes_data)

#print ('people taking 6.004')
#for x in classes_data['6.004']:
#    print (x.print_string())


for peep in peoples_data:
    print ('Person: '+peep.firstname() +' '+peep.lastname())
    x = peep.current_classes_list
    #print (x)
    for x_class in x:
        class_peeps = []
        for student in classes_data[x_class]:
            if student != peep:
                class_peeps.append(student)
        if len(class_peeps) != 0:
            print('people in class ' + x_class)
            for p in class_peeps:
                print ('-'+p.firstname()+' '+p.lastname())
        else:
            print ('no buddies in class '+ x_class)
    print ('-----------------')





