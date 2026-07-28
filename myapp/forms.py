from django import forms
from myapp.models import Student, Department

class StudentForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    age = forms.IntegerField()

    department = forms.ModelChoiceField(
        queryset=Department.objects.all()
    )


class StudentCreationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"