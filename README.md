# Django CRUD Application

A simple Django CRUD (Create, Read, Update, Delete) application demonstrating three different ways of handling forms:

* HTML Forms
* Django `forms.Form`
* Django `forms.ModelForm`

The project is intended for learning Django fundamentals and comparing different approaches to building CRUD applications.

---

## Features

* Add Student
* View Students
* Update Student
* Delete Student
* Responsive and modern UI
* Demonstrates multiple form-handling techniques

---

## Tech Stack

* Python 3.x
* Django
* HTML5
* CSS3
* SQLite (default Django database)

---

## Project Structure

```text
project/
│
├── myapp/
│   ├── migrations/
│   ├── static/
│   │   └── css/
│   ├── templates/
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
└── README.md
```

---

## CRUD Implementations

### 1. HTML Forms

Uses plain HTML form elements.

```html
<input type="text" name="name">
<input type="number" name="age">
<input type="email" name="email">
```

The view retrieves submitted values using:

```python
request.POST.get("name")
```

---

### 2. Django `forms.Form`

Defines fields using Django's `forms.Form`.

```python
class StudentForm(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()
    email = forms.EmailField()
```

Features:

* Validation
* Error handling
* `cleaned_data`
* Manual database save

---

### 3. Django `forms.ModelForm`

Defines the form using a model.

```python
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
```

Features:

* Automatic validation
* Automatic model creation
* `form.save()`
* Less boilerplate code

---

## Installation

Clone the repository.

```bash
git clone <repository-url>
```

Move into the project directory.

```bash
cd project-name
```

Create a virtual environment.

```bash
python -m venv venv
```

Activate the virtual environment.

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install the dependencies.

```bash
pip install -r requirements.txt
```

Apply migrations.

```bash
python manage.py makemigrations
python manage.py migrate
```

Run the development server.

```bash
python manage.py runserver
```

Open your browser and visit:

```
http://127.0.0.1:8000/
```

---

## CRUD Operations

### Create

* HTML Form
* Django Form
* Model Form

### Read

Displays all students in a responsive table.

### Update

Edit student information.

### Delete

Delete a student with confirmation.

---

## Screens

* Student List
* Add Student
* Edit Student
* Delete Student

## License
This project is intended for educational purposes.
