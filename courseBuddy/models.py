from django.db import models

from django.utils.encoding import python_2_unicode_compatible

class Person(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    person_identifier = models.IntegerField(primary_key=True)
    def __str__(self):
        return self.question_text

class Class(models.Model):
    department = models.CharField(max_length=200)
    number = models.IntegerField(default=0)
    def __str__(self):
        return self.department + str(self.number)

class PersonInClass(models.Model):
    person_identifier = models.ForeignKey(Person, on_delete=models.CASCADE)
    class_identifier = models.ForeignKey(Class, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.person_identifier) + ' ' + str(self.class_identifier)