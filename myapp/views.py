from django.shortcuts import render, redirect, get_object_or_404
from myapp.forms import StudentForm, StudentCreationForm
from myapp.models import Student, Department

def student_list(request):
    students = Student.objects.all()
    return render(request, "list-student.html", {"students": students})

from django.shortcuts import render, redirect
from myapp.models import Student, Department

def add_student_html(request):
    departments = Department.objects.all()

    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        email = request.POST.get("email")

        department_id = request.POST.get("department")
        department = Department.objects.get(id=department_id)

        Student.objects.create(
            name=name,
            age=age,
            email=email,
            department=department
        )

        return redirect("students")

    return render(request, "add-student-html.html", {
        "departments": departments
    })

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


def update_student(request, id):
    student = get_object_or_404(Student, id=id)
    departments = Department.objects.all()

    if request.method == "POST":
        student.name = request.POST.get("name")
        student.age = request.POST.get("age")
        student.email = request.POST.get("email")

        department_id = request.POST.get("department")
        student.department = Department.objects.get(id=department_id)

        student.save()

        return redirect("students")

    return render(request, "update.html", {"student": student, "department": department})


def delete_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        student.delete()
        return redirect("students")

    return render(request, "delete.html", {"student": student})
