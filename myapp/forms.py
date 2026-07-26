from django import forms
from myapp.models import Student

class StudentForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    age = forms.IntegerField()


class StudentCreationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"