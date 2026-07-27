from django.urls import path
from myapp.views import student_list, add_student_modelform, add_student_form, add_student_html,update_student,delete_student

urlpatterns = [
    path('', student_list, name='students'),
    path('add_student_modelform/', add_student_modelform, name='add_student_modelform'),
    path('add_student_form/', add_student_form, name='add_student_form'),
    path('add_student_html/', add_student_html, name='add_student_html'),
    path('update_student/<int:id>/',update_student,name='update_student'),
    path('delete_student/<int:id>/',delete_student,name='delete_student'),
]