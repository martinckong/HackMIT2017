from django import forms

class NameForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=100)
    last_name = forms.CharField(label='Last name', max_length=100)
    identifier = forms.IntegerField(label='ID')
    year_school = forms.IntegerField(label='Graduation year')
    classes = forms.CharField(label='Classes (ex: 6.001,6.004)')
