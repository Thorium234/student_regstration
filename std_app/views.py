from django.shortcuts import redirect, render,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Student
from .forms import StudentForm

# Create your views here.
@login_required
def student_list(request):
    student=Student.objects.all()
    return render(request,'std_app/student_list.html',{'students':student})

@login_required
def student_add(request):
    if request.method == 'POST':
        form=StudentForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form=StudentForm()
    return render(request,'std_app/student_add.html',{'form':form})

@login_required
def student_update(request,pk):
    student=get_object_or_404(Student,pk=pk)
    form=StudentForm(request.POST or None,instance=student)
    if request.method == 'POST':
            form=StudentForm(request.POST or None,instance=student)
            if form.is_valid():
                 form.save()
            return redirect('student_list')
    else:
        form=StudentForm(instance=student)
        return render(request,'std_app/student_add.html',{'form':form})

@login_required
def student_delete(request,pk):
    student=get_object_or_404(Student,pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request,'std_app/student_cornfirm_delete.html',{'student':student})

