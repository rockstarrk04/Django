from django import forms

class StudentForm(forms.Form):
    name = forms.CharField(max_length=40)
    email = forms.EmailField()
    mobile_number = forms.IntegerField()
    course = forms.CharField(max_length=40)
    city = forms.CharField(max_length=40)