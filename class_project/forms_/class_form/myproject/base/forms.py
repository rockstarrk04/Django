from django import forms
from .models import StudentModel


class StudentForm(forms.Form):
    Name = forms.CharField()
    Number = forms.IntegerField()
    Email = forms.EmailField()

    def save(self):
        return StudentModel.objects.create(
            name = self.cleaned_data['Name'],   # name = request.POST['Name']
            phone = self.cleaned_data['Number'],
            email = self.cleaned_data['Email']
        )

    def update(self,data):
        data.name = self.cleaned_data['Name']
        data.phone = self.cleaned_data['Number']
        data.email = self.cleaned_data['Email']
        data.save()
        

    