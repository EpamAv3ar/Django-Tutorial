from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()

    class Meta:
        db_table = 'student'

    def __str__(self):
        return self.name