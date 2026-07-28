from django.db import models


class Department(models.Model):
    department_name = models.CharField(max_length=100)

    class Meta:
        db_table = "department"

    def __str__(self):
        return self.department_name


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="students", null=True,
        blank=True
    )

    class Meta:
        db_table = "student"

    def __str__(self):
        return self.name