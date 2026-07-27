from django.shortcuts import render, redirect,get_object_or_404
from myapp.forms import StudentForm, StudentCreationForm
from myapp.models import Student

def student_list(request):
    students = Student.objects.all()
    return render(request, "list-student.html", {"students": students})

def add_student_html(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        email = request.POST.get("email")
        Student.objects.create(
            name=name,
            age=age,
            email=email
        )
        return redirect("students")
    return render(request, "add-student-html.html")

def add_student_form(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            Student.objects.create(
                name=form.cleaned_data["name"],
                age=form.cleaned_data["age"],
                email=form.cleaned_data["email"]
            )
            return redirect("students")
    else:
        form = StudentForm()
    return render(request, "add-student-form.html", {"form": form})

def add_student_modelform(request):
    if request.method == "POST":
        form = StudentCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("students")
    else:
        form = StudentCreationForm()
    return render(request, "add-student-model.html", {"form": form})

def update_student(request,id):
    student=get_object_or_404(Student,id=id)
    if request.method=="POST":
        form=StudentCreationForm(request.POST, instance=student)
        if form.is_valid():
         form.save()
         return redirect('students')
    else:
        form=StudentCreationForm(instance=student)
    return render(request,'update-student.html',{'student':student,'form':form})

def delete_student(request,id):
    student=get_object_or_404(Student,id=id)
    if request.method=="POST":
        student.delete()
        return redirect("students")
    return render(request,"delete-student.html",{"student":student})

