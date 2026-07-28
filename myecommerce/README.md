# Django E-Commerce CRUD Application

A basic Django E-Commerce CRUD application developed for learning Django Generic Class-Based Views and database relationships using Foreign Keys.

The project demonstrates complete CRUD (Create, Read, Update, Delete) operations for **Customer** and **Product** modules.

---

## Features

### Customer Module
- Add Customer
- View Customer List
- Update Customer Details
- Delete Customer

### Product Module
- Add Product
- View Product List
- Update Product Details
- Delete Product

### Additional Features
- ForeignKey relationship between Customer and Product
- Bootstrap 5 responsive user interface
- Django Generic Class-Based Views
- SQLite database
- Django Admin Panel

---

## Tech Stack

- Python 3.x
- Django
- HTML5
- Bootstrap 5
- SQLite3

---

## Database Design

### Customer Table

| Field | Type |
|--------|------|
| Name | CharField |
| Email | EmailField |
| Phone | CharField |
| Address | TextField |

---

### Product Table

| Field | Type |
|--------|------|
| Customer | ForeignKey(Customer) |
| Product Name | CharField |
| Category | CharField |
| Price | DecimalField |
| Quantity | PositiveIntegerField |

---

## Database Relationship

```
Customer (1)
      │
      │
      └──────────────< Product (Many)
```

One customer can purchase multiple products.

---

## Project Structure

```text
myecommerce/
│
├── app1/
│   ├── migrations/
│   ├── templates/
│   │   ├── customer/
│   │   └── product/
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── forms.py
│
├── myecommerce/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── manage.py
├── README.md
└── requirements.txt
```

---

## CRUD Operations

### Customer

- Create Customer
- View Customer
- Update Customer
- Delete Customer

---

### Product

- Create Product
- View Product
- Update Product
- Delete Product

---

## Generic Class-Based Views Used

### Customer

- ListView
- CreateView
- UpdateView
- DeleteView

### Product

- ListView
- CreateView
- UpdateView
- DeleteView

---

## Installation

### Clone the repository

```bash
git clone <repository-url>
```

Move to the project directory.

```bash
cd myecommerce
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

Install the required packages.

```bash
pip install -r requirements.txt
```

Apply migrations.

```bash
python manage.py makemigrations
python manage.py migrate
```

Create a superuser (optional).

```bash
python manage.py createsuperuser
```

Run the server.

```bash
python manage.py runserver
```

Open your browser:

```
http://127.0.0.1:8000/
```


---

## Project Workflow

```
Customer
     │
     ▼
Add Customer
     │
     ▼
Customer List
     │
     ▼
Select Customer
     │
     ▼
Add Product
     │
     ▼
Product List
     │
     ├── Update Product
     │
     └── Delete Product
```

---

## Screens

- Customer List
- Add Customer
- Update Customer
- Delete Customer
- Product List
- Add Product
- Update Product
- Delete Product

---

## Future Enhancements

- Product Image Upload
- Search Functionality
- Product Categories
- Pagination
- Authentication (Login & Logout)
- Shopping Cart
- Order Management


---

## License

This project is developed for educational and learning purposes.