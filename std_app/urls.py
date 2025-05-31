from django.urls import path
from .import views

urlpatterns = [
    path('',views.student_list,name="student_list"),
    path('student_add/',views.student_add,name="student_add"),
    path('update/<int:pk>/',views.student_update,name='student_update'),
    path('delete/<int:pk>/',views.student_delete,name='student_delete'),
]